import os
import math
from pathlib import Path
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import webbrowser

from classifier import analyze_content
from policy_engine import get_policy_for_decision
from crypto_engine import load_or_create_key, encrypt_file
from storage import init_db, log_action
from localization import LANG
from app_meta import APP_NAME, APP_TITLE, APP_VERSION, APP_COMPANY
from api.client import analyze_text_remote

GITHUB_URL = "https://github.com/bylickilabs/SecureAI-PolicyGuard"


class SecureAIPolicyGuardApp:
    def __init__(self, root: tk.Tk):
        self.root = root

        self.current_lang = "de"
        self.trans = LANG[self.current_lang]

        self.api_mode_var = tk.BooleanVar(value=True)
        self.api_url_var = tk.StringVar(value="http://127.0.0.1:8000")

        self.scanning = False
        self.ai_after_id = None
        self.ai_rotation_angle = 0
        self.ai_spin_index = 0
        self.ai_labels = {"idle": "SECUREAI CORE", "active": "SECUREAI CORE – ACTIVE"}
        self.ai_spin = ["Analyzing …"]

        self.row_meta = {}

        self.root.title(APP_TITLE)
        self.root.geometry("1200x700")
        self.root.minsize(1100, 620)

        self._setup_style()
        self._build_ui()
        self._apply_language()
        self._apply_ai_language()
        self._draw_ai_core_idle()

    def _setup_style(self):
        style = ttk.Style(self.root)
        try:
            style.theme_use("clam")
        except tk.TclError:
            pass

        bg = "#05050A"
        fg = "#d9e8ff"
        accent = "#00eaff"
        accent2 = "#ff00c3"
        table = "#111522"

        self.root.configure(bg=bg)

        style.configure("TFrame", background=bg)
        style.configure("TLabel", background=bg, foreground=fg)
        style.configure("Panel.TFrame", background="#0D1020")
        style.configure("Panel.TLabel", background="#0D1020", foreground=fg)

        style.configure(
            "Accent.TButton",
            font=("Segoe UI", 10, "bold"),
            background=accent,
            foreground="#000000",
            padding=8,
            borderwidth=0,
        )
        style.map(
            "Accent.TButton",
            background=[("active", accent2)],
            foreground=[("active", "#ffffff")],
        )

        style.configure(
            "Treeview",
            background=table,
            fieldbackground=table,
            foreground=fg,
            rowheight=24,
        )
        style.map(
            "Treeview",
            background=[("selected", "#1f2940")],
            foreground=[("selected", accent)],
        )

        self.colors = {
            "accent": accent,
            "accent2": accent2,
            "risk_low": "#00c853",
            "risk_mid": "#ffd600",
            "risk_high": "#ff6d00",
            "risk_crit": "#ff1744",
        }

    def _build_ui(self):
        top = ttk.Frame(self.root)
        top.pack(fill=tk.X, padx=10, pady=8)

        left_top = ttk.Frame(top)
        left_top.pack(side=tk.LEFT, fill=tk.X, expand=True)

        self.lbl_title = ttk.Label(left_top, font=("Segoe UI", 18, "bold"))
        self.lbl_sub = ttk.Label(left_top, font=("Segoe UI", 9), foreground="#79a8d1")
        self.lbl_title.pack(anchor="w")
        self.lbl_sub.pack(anchor="w")

        right_top = ttk.Frame(top)
        right_top.pack(side=tk.RIGHT)

        self.ai_canvas = tk.Canvas(
            right_top,
            width=260,
            height=90,
            highlightthickness=0,
            bd=0,
            bg="#05050A",
        )
        self.ai_canvas.pack()

        self.ai_status_label = ttk.Label(
            right_top,
            font=("Segoe UI", 8),
            foreground="#79a8d1",
            anchor="e",
        )
        self.ai_status_label.pack(anchor="e", pady=(2, 0))

        ctrls = ttk.Frame(self.root)
        ctrls.pack(fill=tk.X, padx=10)

        left_ctrls = ttk.Frame(ctrls)
        left_ctrls.pack(side=tk.LEFT, fill=tk.X, expand=True)

        dir_frame = ttk.Frame(left_ctrls)
        dir_frame.pack(fill=tk.X, pady=(0, 2))

        self.lbl_directory = ttk.Label(dir_frame)
        self.lbl_directory.pack(side=tk.LEFT)

        self.entry_directory = ttk.Entry(dir_frame)
        self.entry_directory.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=4)

        self.btn_browse = ttk.Button(dir_frame, command=self.browse_directory)
        self.btn_browse.pack(side=tk.LEFT, padx=4)

        api_frame = ttk.Frame(left_ctrls)
        api_frame.pack(fill=tk.X, pady=(2, 0))

        self.chk_api = ttk.Checkbutton(api_frame, variable=self.api_mode_var)
        self.chk_api.pack(side=tk.LEFT, padx=(0, 4))

        self.lbl_api_mode = ttk.Label(api_frame)
        self.lbl_api_mode.pack(side=tk.LEFT)

        self.lbl_api_url = ttk.Label(api_frame)
        self.lbl_api_url.pack(side=tk.LEFT, padx=(10, 2))

        self.entry_api_url = ttk.Entry(api_frame, textvariable=self.api_url_var, width=40)
        self.entry_api_url.pack(side=tk.LEFT, padx=4)

        right_ctrls = ttk.Frame(ctrls)
        right_ctrls.pack(side=tk.RIGHT)

        self.btn_lang_de = ttk.Button(right_ctrls, width=4, command=lambda: self.set_language("de"))
        self.btn_lang_de.pack(side=tk.RIGHT, padx=2)

        self.btn_lang_en = ttk.Button(right_ctrls, width=4, command=lambda: self.set_language("en"))
        self.btn_lang_en.pack(side=tk.RIGHT, padx=2)

        self.btn_github = ttk.Button(right_ctrls, command=self.open_github)
        self.btn_github.pack(side=tk.RIGHT, padx=4)

        self.btn_info = ttk.Button(right_ctrls, command=self.show_info)
        self.btn_info.pack(side=tk.RIGHT, padx=4)

        scan_frame = ttk.Frame(self.root)
        scan_frame.pack(fill=tk.X, padx=10, pady=(5, 5))

        self.btn_scan = ttk.Button(
            scan_frame,
            style="Accent.TButton",
            command=self.run_scan,
        )
        self.btn_scan.pack(anchor="w")

        panel = ttk.Frame(self.root, style="Panel.TFrame")
        panel.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        self.lbl_matrix = ttk.Label(
            panel,
            style="Panel.TLabel",
            font=("Segoe UI", 11, "bold"),
        )
        self.lbl_matrix.pack(anchor="w", pady=(4, 4))

        tree_frame = ttk.Frame(panel, style="Panel.TFrame")
        tree_frame.pack(fill=tk.BOTH, expand=True)

        columns = ("file", "classification", "risk", "action")
        self.tree = ttk.Treeview(
            tree_frame,
            columns=columns,
            show="headings",
            selectmode="browse",
        )
        self.tree.column("file", width=600, anchor="w")
        self.tree.column("classification", width=180, anchor="w")
        self.tree.column("risk", width=80, anchor="center")
        self.tree.column("action", width=160, anchor="w")

        vsb = ttk.Scrollbar(tree_frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=vsb.set)

        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        vsb.pack(side=tk.RIGHT, fill=tk.Y)

        self.tree.tag_configure("risk_low", foreground=self.colors["risk_low"])
        self.tree.tag_configure("risk_mid", foreground=self.colors["risk_mid"])
        self.tree.tag_configure("risk_high", foreground=self.colors["risk_high"])
        self.tree.tag_configure("risk_crit", foreground=self.colors["risk_crit"])

        self.tree.bind("<Double-1>", self.show_details)

        status_frame = ttk.Frame(self.root)
        status_frame.pack(fill=tk.X, padx=10, pady=5)

        self.status_label = ttk.Label(status_frame, anchor="w")
        self.status_label.pack(fill=tk.X, expand=True)

    def _apply_language(self):
        tr = self.trans

        self.root.title(tr["window_title"])
        self.lbl_title.config(text=APP_NAME)
        self.lbl_sub.config(text=f"{APP_VERSION} – {APP_COMPANY}")

        self.lbl_directory.config(text=tr["label_directory"])
        self.btn_browse.config(text=tr["button_browse"])
        self.btn_scan.config(text=tr["button_scan"])
        self.btn_info.config(text=tr["button_info"])
        self.btn_github.config(text=tr["button_github"])

        self.btn_lang_de.config(text=tr["lang_de"])
        self.btn_lang_en.config(text=tr["lang_en"])

        self.lbl_api_mode.config(text=tr["label_api_mode"])
        self.lbl_api_url.config(text=tr["label_api_url"])

        self.tree.heading("file", text=tr["column_file"])
        self.tree.heading("classification", text=tr["column_classification"])
        self.tree.heading("risk", text=tr["column_risk"])
        self.tree.heading("action", text=tr["column_action"])

        self.lbl_matrix.config(text=tr["column_classification"])
        self.status_label.config(text=tr["status_ready"])

    def _apply_ai_language(self):
        tr = self.trans
        self.ai_labels = {
            "idle": tr["ai_core_idle"],
            "active": tr["ai_core_active_label"],
        }
        self.ai_spin = tr["ai_spinner_frames"]
        self.ai_spin_index = 0
        self.ai_status_label.config(text=self.ai_labels["idle"])

    def set_language(self, lang_code: str):
        if lang_code not in LANG:
            return
        self.current_lang = lang_code
        self.trans = LANG[lang_code]
        self._apply_language()
        self._apply_ai_language()
        self._draw_ai_core_idle()

    def _draw_ai_core_idle(self):
        c = self.ai_canvas
        c.delete("all")
        cx, cy = 190, 45

        c.create_text(
            20,
            20,
            text=self.ai_labels.get("idle", "SECUREAI CORE"),
            anchor="w",
            fill="#76d5ff",
            font=("Consolas", 9, "bold"),
        )

        c.create_oval(
            cx - 25,
            cy - 25,
            cx + 25,
            cy + 25,
            outline=self.colors["accent"],
            width=2,
        )
        c.create_oval(
            cx - 35,
            cy - 35,
            cx + 35,
            cy + 35,
            outline=self.colors["accent2"],
            width=1,
        )

        c.create_oval(
            cx - 10,
            cy - 10,
            cx + 10,
            cy + 10,
            fill="#050b16",
            outline=self.colors["accent"],
            width=1,
        )

    def _start_ai_animation(self):
        if self.scanning:
            return
        self.scanning = True
        self._ai_animation_step()

    def _stop_ai_animation(self):
        self.scanning = False
        if self.ai_after_id:
            self.root.after_cancel(self.ai_after_id)
            self.ai_after_id = None
        self.ai_status_label.config(text=self.ai_labels.get("idle", "SECUREAI CORE"))
        self._draw_ai_core_idle()

    def _ai_animation_step(self):
        if not self.scanning:
            return

        c = self.ai_canvas
        c.delete("all")
        cx, cy = 190, 45

        c.create_text(
            20,
            20,
            text=self.ai_labels.get("active", "SECUREAI CORE – ACTIVE"),
            anchor="w",
            fill=self.colors["accent"],
            font=("Consolas", 9, "bold"),
        )

        radius = 38
        for i in range(10):
            angle = math.radians(self.ai_rotation_angle + i * 36)
            x = cx + math.cos(angle) * radius
            y = cy + math.sin(angle) * radius
            c.create_oval(
                x - 3,
                y - 3,
                x + 3,
                y + 3,
                fill=self.colors["accent"],
                outline="",
            )

        c.create_oval(
            cx - 12,
            cy - 12,
            cx + 12,
            cy + 12,
            fill="#050b16",
            outline=self.colors["accent2"],
            width=1,
        )

        if self.ai_spin:
            spin_text = self.ai_spin[self.ai_spin_index % len(self.ai_spin)]
            self.ai_status_label.config(text=spin_text)
            self.ai_spin_index += 1

        self.ai_rotation_angle = (self.ai_rotation_angle + 8) % 360
        self.ai_after_id = self.root.after(80, self._ai_animation_step)

    def browse_directory(self):
        directory = filedialog.askdirectory()
        if directory:
            self.entry_directory.delete(0, tk.END)
            self.entry_directory.insert(0, directory)

    def run_scan(self):
        tr = self.trans
        base_dir_text = self.entry_directory.get().strip()

        if not base_dir_text:
            messagebox.showwarning(tr["msg_no_dir_title"], tr["msg_no_dir_body"])
            return

        base_dir = Path(base_dir_text)
        if not base_dir.exists():
            messagebox.showwarning(tr["msg_no_dir_title"], tr["msg_no_dir_body"])
            return

        for item in self.tree.get_children():
            self.tree.delete(item)
        self.row_meta.clear()

        self.status_label.config(text=tr["status_scanning"])
        self._start_ai_animation()
        self.root.update_idletasks()

        conn = init_db(base_dir)
        fernet = load_or_create_key(base_dir)

        processed = 0

        try:
            for root_dir, dirs, files in os.walk(base_dir):
                for filename in files:
                    if not filename.lower().endswith(".txt"):
                        continue

                    full_path = Path(root_dir) / filename
                    try:
                        text = full_path.read_text(encoding="utf-8", errors="ignore")
                    except Exception as e:
                        print(f"[WARN] Could not read file {full_path}: {e}")
                        continue

                    use_api = self.api_mode_var.get()
                    classification = None
                    risk_score = 0
                    entities = []

                    if use_api:
                        try:
                            data = analyze_text_remote(text, self.api_url_var.get())
                            classification = data["classification"]
                            risk_score = int(data["risk_score"])
                            entities = data.get("entities", [])
                        except Exception as e:
                            print(f"[ERROR] API call failed, falling back to local: {e}")
                            self.status_label.config(text=tr["status_api_error"])
                            decision = analyze_content(text)
                            classification = decision["classification"]
                            risk_score = int(decision["risk_score"])
                            entities = decision["entities"]
                    else:
                        decision = analyze_content(text)
                        classification = decision["classification"]
                        risk_score = int(decision["risk_score"])
                        entities = decision["entities"]

                    policy = get_policy_for_decision(classification, risk_score, entities)

                    action = "NONE"
                    if policy.get("encrypt"):
                        target_dir = base_dir / policy["target_dir"]
                        target_dir.mkdir(parents=True, exist_ok=True)
                        target_file = target_dir / (full_path.name + ".enc")
                        try:
                            encrypt_file(full_path, target_file, fernet)
                            action = "ENCRYPTED"
                        except Exception as e:
                            print(f"[ERROR] Encryption failed for {full_path}: {e}")
                            action = "ERROR"
                    elif policy.get("log_only"):
                        action = "LOG_ONLY"

                    log_action(
                        conn,
                        str(full_path),
                        classification,
                        action,
                        risk_score,
                        len(entities),
                        "",
                    )

                    tag = self._tag_for_risk(risk_score)
                    class_label = tr.get(f"classification_{classification}", classification)
                    action_label = tr.get(f"action_{action}", action)

                    item_id = self.tree.insert(
                        "",
                        tk.END,
                        values=(str(full_path), class_label, f"{risk_score}%", action_label),
                        tags=(tag,),
                    )

                    self.row_meta[item_id] = {
                        "entities": entities,
                        "risk": risk_score,
                        "classification": class_label,
                        "file": str(full_path),
                    }

                    processed += 1
                    self.root.update()

        except Exception as e:
            print(f"[ERROR] Scan failed: {e}")
            self.status_label.config(text=tr["status_error"])
            self._stop_ai_animation()
            return

        self._stop_ai_animation()
        self.status_label.config(text=tr["status_done"])
        messagebox.showinfo(
            tr["msg_scan_finished_title"],
            tr["msg_scan_finished_body"].format(count=processed),
        )

    def _tag_for_risk(self, score: int) -> str:
        if score < 30:
            return "risk_low"
        if score < 60:
            return "risk_mid"
        if score < 80:
            return "risk_high"
        return "risk_crit"

    def show_details(self, event):
        tr = self.trans
        item_id = self.tree.identify_row(event.y)
        if not item_id:
            return

        meta = self.row_meta.get(item_id)
        if not meta:
            return

        file_path = meta["file"]
        classification = meta["classification"]
        risk = meta["risk"]
        entities = meta["entities"]

        explanation_lines = [
            tr["ai_explain_header"],
            tr["ai_explain_risk"].format(score=risk),
        ]

        if entities:
            explanation_lines.append("")
            explanation_lines.append(tr["ai_explain_entities_prefix"])
            counts = {}
            for label, _value in entities:
                counts[label] = counts.get(label, 0) + 1
            for label, count in counts.items():
                mapped = tr.get(f"entity_{label}", label)
                explanation_lines.append(
                    tr["ai_explain_entities_item"].format(label=mapped, count=count)
                )
            explanation_lines.append("")
            explanation_lines.append(tr["ai_explain_recommend_encrypt"])
        else:
            explanation_lines.append("")
            explanation_lines.append(tr["ai_explain_no_entities"])
            explanation_lines.append("")
            explanation_lines.append(tr["ai_explain_recommend_monitor"])

        detail_text = (
            f"{tr['detail_file']}: {file_path}\n"
            f"{tr['detail_classification']}: {classification}\n"
            f"{tr['detail_risk']}: {risk}%\n\n"
            + "\n".join(explanation_lines)
        )

        messagebox.showinfo(tr["detail_title"], detail_text)

    def show_info(self):
        tr = self.trans
        messagebox.showinfo(tr["info_title"], tr["info_body"])

    def open_github(self):
        webbrowser.open(GITHUB_URL)

def main():
    root = tk.Tk()
    app = SecureAIPolicyGuardApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
