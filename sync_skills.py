#!/usr/bin/env python3
import os
import subprocess
import sys

SOURCE_AGENTS = "/home/shahin/ai-skills/.agents"
SOURCE_SKILLS = os.path.join(SOURCE_AGENTS, "skills")
SOURCE_DESCRIPTIONS = os.path.join(SOURCE_AGENTS, "DESCRIPTIONS.md")

TARGET_AGENTS_DIRS = [
    "/home/shahin/.agents",
    "/home/shahin/aiac-res/.agents",
    "/home/shahin/cv-analysis/.agents",
    "/home/shahin/distill/.agents",
    "/home/shahin/document_AI/.agents",
    "/home/shahin/ml-project/.agents",
    "/home/shahin/naic/dlp-elastic/.agents",
    "/mnt/c/Vaults/CvAnalysis/.agents",
    "/mnt/c/Vaults/DistillVault/.agents",
    "/mnt/c/Vaults/DlpVault/.agents",
    "/mnt/c/Vaults/aiac-res/.agents",
    "/mnt/c/Vaults/doc-analysis/.agents",
    "/mnt/c/Vaults/ml-project/.agents",
]

def main():
    if not os.path.exists(SOURCE_SKILLS):
        print(f"Error: Source skills directory does not exist: {SOURCE_SKILLS}")
        sys.exit(1)

    source_skills_count = len([
        d for d in os.listdir(SOURCE_SKILLS)
        if os.path.isdir(os.path.join(SOURCE_SKILLS, d))
    ])

    print(f"Starting sync from {SOURCE_AGENTS}")
    print(f"Source contains {source_skills_count} skill directories.")
    print("-" * 60)

    all_passed = True

    for target in TARGET_AGENTS_DIRS:
        target_skills = os.path.join(target, "skills")
        target_desc = os.path.join(target, "DESCRIPTIONS.md")

        print(f"Syncing to: {target} ...")
        os.makedirs(target_skills, exist_ok=True)

        # Sync skills directory using rsync for reliable cross-mount sync
        rsync_cmd = ["rsync", "-rlt", "--delete", "--no-perms", "--no-owner", "--no-group", SOURCE_SKILLS + "/", target_skills + "/"]
        res = subprocess.run(rsync_cmd, capture_output=True, text=True)
        if res.returncode != 0:
            print(f"  [ERROR] rsync failed for {target}: {res.stderr}")
            all_passed = False
            continue

        # Sync DESCRIPTIONS.md if exists
        if os.path.exists(SOURCE_DESCRIPTIONS):
            subprocess.run(["cp", SOURCE_DESCRIPTIONS, target_desc], check=True)

        # Sync agents and agents-codex directories if they exist
        for agent_dir_name in ["agents", "agents-codex"]:
            src_sub = os.path.join(SOURCE_AGENTS, agent_dir_name)
            if os.path.exists(src_sub):
                tgt_sub = os.path.join(target, agent_dir_name)
                os.makedirs(tgt_sub, exist_ok=True)
                subprocess.run(["rsync", "-rlt", "--delete", "--no-perms", "--no-owner", "--no-group", src_sub + "/", tgt_sub + "/"], check=True)

        copied_count = len([
            d for d in os.listdir(target_skills)
            if os.path.isdir(os.path.join(target_skills, d))
        ])
        if copied_count == source_skills_count:
            print(f"  [OK] Successfully synced {copied_count}/{source_skills_count} skills to {target_skills}")
        else:
            print(f"  [WARNING] Count mismatch: {copied_count}/{source_skills_count} in {target_skills}")
            all_passed = False

    print("-" * 60)
    if all_passed:
        print(f"ALL SYNC TARGETS UPDATED SUCCESSFULLY WITH {source_skills_count} SKILLS!")
    else:
        print("SOME TARGETS HAD ISSUES. CHECK LOGS ABOVE.")

if __name__ == "__main__":
    main()
