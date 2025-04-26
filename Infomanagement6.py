def manage_information():
    print("📁 Information Management Expert System")
    print("Answer the following to get storage & security suggestions.\n")

    info_type = input("Enter type of information (confidential / public / medical / financial): ").strip().lower()
    is_frequently_accessed = input("Is this data frequently accessed? (yes/no): ").strip().lower()
    is_sensitive = input("Is this data sensitive or private? (yes/no): ").strip().lower()

    print("\n🧠 Expert Recommendation:")

    if info_type == 'confidential' or is_sensitive == 'yes':
        print("🔐 Store in an encrypted database with restricted access.")
        print("✅ Enable two-factor authentication.")
        if is_frequently_accessed == 'yes':
            print("📦 Use a secure cloud-based storage with auditing.")
        else:
            print("📁 Archive in secure offline storage.")

    elif info_type == 'medical':
        print("🩺 Use HIPAA-compliant systems.")
        print("🔐 Ensure data is encrypted both at rest and in transit.")
        print("👥 Limit access to authorized medical staff.")

    elif info_type == 'financial':
        print("💰 Use encrypted databases with secure backup.")
        print("📊 Use audit logs and access control.")
        if is_frequently_accessed == 'yes':
            print("📈 Consider cloud-hosted solutions with real-time analytics.")

    elif info_type == 'public':
        print("🌐 Public info can be stored on web servers or document repositories.")
        print("🛡️ Still monitor for unauthorized edits.")

    else:
        print("⚠️ Unknown type. Store cautiously and monitor usage.")

# Run
if __name__ == "__main__":
    manage_information()
