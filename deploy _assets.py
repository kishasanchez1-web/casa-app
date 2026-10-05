import os
import subprocess
import sys

# Define configuration parameters
FOLDER_NAME = "casa-by-luxe-app"
REPO_NAME = "casa-app"

# 1. Ask user for their GitHub Username to map the destination URL
print("◈ Luxera Solutions - Automated Deployment Script ◈\n")
github_username = input("Enter your GitHub Username: ").strip()
if not github_username:
    print("[Error] GitHub username cannot be empty.")
    sys.exit(1)

# 2. Setup the directory structure
if not os.path.exists(FOLDER_NAME):
    os.makedirs(FOLDER_NAME)
    print(f"[Success] Created local directory: {FOLDER_NAME}")
else:
    print(f"[Info] Local directory {FOLDER_NAME} already exists. Proceeding...")

os.chdir(FOLDER_NAME)

# 3. Code Asset payloads from the past 48 hours
html_app_code = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Casa By Luxe - My Legacy Vision</title>
    <script src="https://tailwindcss.com"></script>
    <link href="https://googleapis.com" rel="stylesheet">
    <style>
        body { font-family: 'Plus Jakarta Sans', sans-serif; background-color: #FAF9F6; }
        .serif-title { font-family: 'Playfair Display', serif; }
    </style>
</head>
<body class="text-neutral-800 antialiased min-h-screen pb-24">
    <header class="bg-white border-b border-neutral-100 sticky top-0 z-50 px-4 py-4 shadow-sm">
        <div class="max-w-md mx-auto flex justify-between items-center">
            <div>
                <h1 class="serif-title text-xl font-semibold tracking-wide text-neutral-900">Casa By Luxe</h1>
                <p class="text-xs text-neutral-400 tracking-wider uppercase">Life Design Matrix</p>
            </div>
            <div id="completionBadge" class="bg-neutral-900 text-white text-xs font-semibold px-3 py-1.5 rounded-full">0% Designed</div>
        </div>
    </header>
    <main class="max-w-md mx-auto px-4 mt-6 space-y-8">
        <section class="bg-white rounded-3xl p-6 border border-neutral-100 shadow-sm space-y-4">
            <h2 class="serif-title text-lg font-medium text-neutral-900">Vision Architecture Balance</h2>
            <div id="chartContainer" class="h-44 w-full flex items-end justify-between px-4 pt-4 border-b border-neutral-100 pb-2">
                <div class="flex flex-col items-center w-12"><div id="bar-wealth" class="w-full bg-amber-700/80 rounded-t-lg h-2" style="height: 5%"></div><span class="text-[10px] uppercase tracking-wider text-neutral-400 mt-2 font-medium">Wealth</span></div>
                <div class="flex flex-col items-center w-12"><div id="bar-health" class="w-full bg-emerald-800/80 rounded-t-lg h-2" style="height: 5%"></div><span class="text-[10px] uppercase tracking-wider text-neutral-400 mt-2 font-medium">Health</span></div>
                <div class="flex flex-col items-center w-12"><div id="bar-spaces" class="w-full bg-stone-600/80 rounded-t-lg h-2" style="height: 5%"></div><span class="text-[10px] uppercase tracking-wider text-neutral-400 mt-2 font-medium">Spaces</span></div>
                <div class="flex flex-col items-center w-12"><div id="bar-legacy" class="w-full bg-neutral-800/80 rounded-t-lg h-2" style="height: 5%"></div><span class="text-[10px] uppercase tracking-wider text-neutral-400 mt-2 font-medium">Legacy</span></div>
            </div>
        </section>
        <section class="space-y-6">
            <div class="bg-white rounded-3xl p-6 border border-neutral-100 shadow-sm space-y-4">
                <h3 class="serif-title text-md font-medium text-neutral-900">Financial Independence & Flow</h3>
                <textarea id="input-wealth" oninput="saveAndUpdate()" placeholder="Describe your exact cash flow models..." class="w-full h-24 p-4 text-sm bg-neutral-50 rounded-2xl border focus:outline-none text-neutral-700"></textarea>
            </div>
            <div class="bg-white rounded-3xl p-6 border border-neutral-100 shadow-sm space-y-4">
                <h3 class="serif-title text-md font-medium text-neutral-900">Physical Mastery & Energy</h3>
                <textarea id="input-health" oninput="saveAndUpdate()" placeholder="Detail your daily physical energy..." class="w-full h-24 p-4 text-sm bg-neutral-50 rounded-2xl border focus:outline-none text-neutral-700"></textarea>
            </div>
            <div class="bg-white rounded-3xl p-6 border border-neutral-100 shadow-sm space-y-4">
                <h3 class="serif-title text-md font-medium text-neutral-900">Environment & Living Spaces</h3>
                <textarea id="input-spaces" oninput="saveAndUpdate()" placeholder="Describe your sanctuary..." class="w-full h-24 p-4 text-sm bg-neutral-50 rounded-2xl border focus:outline-none text-neutral-700"></textarea>
            </div>
            <div class="bg-white rounded-3xl p-6 border border-neutral-100 shadow-sm space-y-4">
                <h3 class="serif-title text-md font-medium text-neutral-900">Scalable Influence & Creations</h3>
                <textarea id="input-legacy" oninput="saveAndUpdate()" placeholder="What multi-format assets have you finished..." class="w-full h-24 p-4 text-sm bg-neutral-50 rounded-2xl border focus:outline-none text-neutral-700"></textarea>
            </div>
        </section>
    </main>
    <footer class="fixed bottom-0 left-0 right-0 bg-white/80 backdrop-blur-md border-t border-neutral-100 py-3 text-center px-4">
        <a href="https://github.com" target="_blank" class="text-[11px] tracking-wider uppercase text-neutral-400 font-medium">Engineered By <span class="text-neutral-900 font-semibold underline">Casa By Luxe Software Systems</span></a>
    </footer>
    <script>
        const pillars = ['wealth', 'health', 'spaces', 'legacy'];
        function saveAndUpdate() {
            let totalLength = 0; let targetLength = 150;
            pillars.forEach(pillar => {
                const val = document.getElementById(`input-${pillar}`).value;
                localStorage.setItem(`cbl_vision_${pillar}`, val);
                const cur = Math.min(val.length, targetLength);
                document.getElementById(`bar-${pillar}`).style.height = `${Math.max((cur / targetLength) * 100, 5)}%`;
                totalLength += cur;
            });
            document.getElementById('completionBadge').innerText = `${Math.round((totalLength / (targetLength * pillars.length)) * 100)}% Aligned`;
        }
        window.onload = function() {
            pillars.forEach(p => { const val = localStorage.getItem(`cbl_vision_${p}`); if(val) document.getElementById(`input-${p}`).value = val; });
            saveAndUpdate();
        }
    </script>
</body>
</html>"""

html_dispute_code = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Luxera Solutions - Automated Dispute Engine</title>
    <script src="https://tailwindcss.com"></script>
    <link href="https://googleapis.com" rel="stylesheet">
    <style> body { font-family: 'Plus Jakarta Sans', sans-serif; background-color: #0B0F19; } </style>
</head>
<body class="text-slate-200 antialiased min-h-screen pb-24">
    <header class="border-b border-slate-800 bg-slate-900/50 backdrop-blur-md sticky top-0 z-50 px-6 py-4">
        <div class="max-w-6xl mx-auto flex justify-between items-center">
            <h1 class="text-xl font-bold tracking-tight text-white"><span class="text-indigo-500">◈</span> Luxera Solutions</h1>
            <span class="text-xs font-semibold uppercase tracking-wider text-slate-400">Live API Bridge Active</span>
        </div>
    </header>
    <main class="max-w-6xl mx-auto px-6 mt-8 grid grid-cols-1 lg:grid-cols-3 gap-8">
        <div class="space-y-6 lg:col-span-1">
            <div class="bg-gradient-to-br from-slate-900 to-slate-950 p-6 rounded-3xl border border-slate-800 shadow-xl space-y-4">
                <h2 class="text-sm font-semibold text-slate-400 uppercase tracking-wider">Revenue Protection Overview</h2>
                <p id="totalRecovered" class="text-4xl font-extrabold text-white">$0.00</p>
                <button onclick="shareStats()" class="w-full bg-slate-800 hover:bg-slate-700 text-white text-xs font-semibold py-3 rounded-xl transition-all">𝕏 Share Capital Milestone to LinkedIn / X</button>
            </div>
            <div class="bg-slate-900/40 p-6 rounded-3xl border border-slate-800/80 space-y-4">
                <h3 class="text-xs font-bold uppercase tracking-wider text-slate-400">Order Exception Simulator</h3>
                <button onclick="simulateTicket(142.50, 'Transit Damage')" class="w-full text-xs bg-slate-900 p-3 rounded-xl border border-slate-800 text-amber-400 font-medium">🚨 Transit Damage Ticket</button>
            </div>
        </div>
        <div class="lg:col-span-2">
            <div id="consoleLog" class="bg-slate-900/60 rounded-3xl p-6 border border-slate-800 h-96 overflow-y-auto text-xs font-mono text-slate-400">// System waiting for webhook telemetry...</div>
        </div>
    </main>
    <footer class="fixed bottom-0 left-0 right-0 bg-slate-950/80 backdrop-blur-md border-t border-slate-900 py-4 text-center px-4">
        <p class="text-[11px] tracking-wider uppercase text-slate-500 font-medium">Protected & Verified Asset Front by <span class="text-white font-bold underline">Luxera Solutions</span></p>
    </footer>
    <script>
        let balance = 0.00;
        function simulateTicket(cost, type) {
            balance += cost; document.getElementById('totalRecovered').innerText = `$${balance.toFixed(2)}`;
            const log = document.getElementById('consoleLog');
            if(log.innerText.includes("// System waiting")) log.innerHTML = "";
