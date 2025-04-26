def ask_yes_no(question):
    while True:
        answer = input(question + " (yes/no): ").strip().lower()
        if answer in ['yes', 'no']:
            return answer == 'yes'
        else:
            print("Please answer with 'yes' or 'no'.")

def diagnose_issue():
    print("📞 Help Desk Expert System")
    print("Answer the following questions to diagnose your issue...\n")

    if ask_yes_no("Is your computer not turning on?"):
        if ask_yes_no("Do you hear any beeping sounds?"):
            print("🔧 Suggestion: Check the RAM. Reseat or replace it.")
        else:
            print("🔧 Suggestion: Check the power cable and SMPS unit.")
        return

    if ask_yes_no("Is your internet not working?"):
        if ask_yes_no("Is the Wi-Fi connected but no internet access?"):
            print("🔧 Suggestion: Try restarting your router. If the issue persists, contact your ISP.")
        else:
            print("🔧 Suggestion: Check if Wi-Fi is turned on or try connecting via LAN.")
        return

    if ask_yes_no("Is your system running very slow?"):
        if ask_yes_no("Do you have many programs open at once?"):
            print("🔧 Suggestion: Close unused applications or upgrade your RAM.")
        else:
            print("🔧 Suggestion: Run a virus scan or check for startup programs slowing down the system.")
        return

    if ask_yes_no("Is your screen frozen or unresponsive?"):
        print("🔧 Suggestion: Try pressing Ctrl+Alt+Del and restart. If it persists, check for driver updates.")
        return

    print("🤖 Unable to diagnose the issue with the current information.")
    print("Please contact technical support for more help.")

# ===== MAIN CODE =====
if __name__ == '__main__':
    diagnose_issue()
