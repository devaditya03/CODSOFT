"""
📘 UNIQUE CONTACT BOOK APPLICATION
A feature-rich contact management system with persistent storage
"""

import json
import os
from typing import List, Dict

class ContactBook:
    def __init__(self, data_file: str = "contacts_data.json"):
        self.data_file = data_file
        self.contacts: List[Dict] = self.load_contacts()
    
    def load_contacts(self) -> List[Dict]:
        """Load contacts from JSON file"""
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except (json.JSONDecodeError, IOError):
                return []
        return []
    
    def save_contacts(self) -> bool:
        """Save contacts to JSON file"""
        try:
            with open(self.data_file, 'w', encoding='utf-8') as f:
                json.dump(self.contacts, f, indent=2, ensure_ascii=False)
            return True
        except IOError:
            return False
    
    def add_contact(self, name: str, phone: str, email: str, address: str) -> bool:
        """Add a new contact to the contact book"""
        if not name or not phone:
            print("❌ Error: Name and phone number are required.")
            return False
        
        if any(contact['phone'] == phone for contact in self.contacts):
            print("❌ Error: Phone number already exists in contacts.")
            return False
        
        contact = {
            'name': name.strip(),
            'phone': phone.strip(),
            'email': email.strip(),
            'address': address.strip()
        }
        
        self.contacts.append(contact)
        if self.save_contacts():
            print(f"✅ Contact '{name}' added successfully!")
            return True
        else:
            print("❌ Error: Failed to save contact.")
            return False
    
    def view_contacts(self) -> None:
        """Display all contacts in a formatted list"""
        if not self.contacts:
            print("📭 No contacts found. Add some contacts first!")
            return
        
        print("\n" + "="*60)
        print("📖 CONTACT LIST")
        print("="*60)
        print(f"| {'#':<3} | {'Name':<25} | {'Phone':<15} |")
        print("-"*60)
        
        for idx, contact in enumerate(self.contacts, 1):
            name = contact['name'][:24]
            phone = contact['phone'][:14]
            print(f"| {idx:<3} | {name:<25} | {phone:<15} |")
        
        print("="*60)
        print(f"Total contacts: {len(self.contacts)}")
        print()
    
    def search_contacts(self, search_term: str) -> List[Dict]:
        """Search contacts by name or phone number"""
        if not search_term:
            return []
        
        search_lower = search_term.lower().strip()
        results = []
        
        for contact in self.contacts:
            if search_lower in contact['name'].lower() or search_lower in contact['phone']:
                results.append(contact)
        
        return results
    
    def display_contact_details(self, contact: Dict) -> None:
        """Display detailed information for a single contact"""
        print("\n" + "-"*50)
        print("📞 CONTACT DETAILS")
        print("-"*50)
        print(f"  Name:    {contact['name']}")
        print(f"  Phone:   {contact['phone']}")
        print(f"  Email:   {contact['email'] if contact['email'] else 'Not provided'}")
        print(f"  Address: {contact['address'] if contact['address'] else 'Not provided'}")
        print("-"*50)
    
    def update_contact(self, search_term: str) -> bool:
        """Update contact details by searching for the contact"""
        results = self.search_contacts(search_term)
        
        if not results:
            print(f"❌ No contact found matching '{search_term}'")
            return False
        
        if len(results) > 1:
            print(f"\n⚠️  Multiple contacts found matching '{search_term}':")
            for idx, contact in enumerate(results, 1):
                print(f"  {idx}. {contact['name']} - {contact['phone']}")
            
            try:
                choice = int(input("Which contact to update? Enter number: "))
                if choice < 1 or choice > len(results):
                    print("❌ Invalid choice.")
                    return False
                contact = results[choice - 1]
            except ValueError:
                print("❌ Invalid input.")
                return False
        else:
            contact = results[0]
        
        self.display_contact_details(contact)
        
        print("\nEnter new details (leave blank to keep current):")
        new_name = input(f"  Name ({contact['name']}): ").strip()
        new_phone = input(f"  Phone ({contact['phone']}): ").strip()
        new_email = input(f"  Email ({contact['email']}): ").strip()
        new_address = input(f"  Address ({contact['address']}): ").strip()
        
        if new_name:
            contact['name'] = new_name
        if new_phone:
            if any(c['phone'] == new_phone and c['name'] != contact['name'] for c in self.contacts):
                print("❌ Error: Phone number already exists in other contacts.")
                return False
            contact['phone'] = new_phone
        if new_email:
            contact['email'] = new_email
        if new_address:
            contact['address'] = new_address
        
        if self.save_contacts():
            print("✅ Contact updated successfully!")
            self.display_contact_details(contact)
            return True
        else:
            print("❌ Error: Failed to update contact.")
            return False
    
    def delete_contact(self, search_term: str) -> bool:
        """Delete a contact by searching for it"""
        results = self.search_contacts(search_term)
        
        if not results:
            print(f"❌ No contact found matching '{search_term}'")
            return False
        
        if len(results) > 1:
            print(f"\n⚠️  Multiple contacts found matching '{search_term}':")
            for idx, contact in enumerate(results, 1):
                print(f"  {idx}. {contact['name']} - {contact['phone']}")
            
            try:
                choice = int(input("Which contact to delete? Enter number: "))
                if choice < 1 or choice > len(results):
                    print("❌ Invalid choice.")
                    return False
                contact = results[choice - 1]
            except ValueError:
                print("❌ Invalid input.")
                return False
        else:
            contact = results[0]
        
        self.display_contact_details(contact)
        
        confirm = input("Are you sure you want to delete this contact? (yes/no): ").strip().lower()
        if confirm != 'yes':
            print("❌ Deletion cancelled.")
            return False
        
        self.contacts.remove(contact)
        if self.save_contacts():
            print(f"✅ Contact '{contact['name']}' deleted successfully!")
            return True
        else:
            print("❌ Error: Failed to delete contact.")
            return False


def print_menu() -> None:
    """Display the main menu"""
    print("\n" + "="*60)
    print("📘 UNIQUE CONTACT BOOK APPLICATION")
    print("="*60)
    print("  1. ➕ Add New Contact")
    print("  2. 📖 View All Contacts")
    print("  3. 🔍 Search Contact")
    print("  4. ✏️ Update Contact")
    print("  5. ❌ Delete Contact")
    print("  6. 🚪 Exit")
    print("="*60)


def get_input(name: str, required: bool = False) -> str:
    """Get user input with optional requirement validation"""
    while True:
        value = input(f"  {name}: ").strip()
        if value or not required:
            return value
        print(f"  ⚠️  {name} is required. Please enter a value.")


def main():
    """Main function to run the contact book application"""
    contact_book = ContactBook()
    
    print("\n" + "🎉" * 20)
    print("Welcome to the UNIQUE Contact Book Application!")
    print("🎉" * 20)
    
    while True:
        print_menu()
        
        choice = input("Enter your choice (1-6): ").strip()
        
        if choice == '1':
            print("\n➕ ADD NEW CONTACT")
            print("-"*40)
            name = get_input("Name", required=True)
            phone = get_input("Phone Number", required=True)
            email = get_input("Email")
            address = get_input("Address")
            
            contact_book.add_contact(name, phone, email, address)
        
        elif choice == '2':
            contact_book.view_contacts()
        
        elif choice == '3':
            print("\n🔍 SEARCH CONTACT")
            print("-"*40)
            search_term = get_input("Enter name or phone number to search", required=True)
            results = contact_book.search_contacts(search_term)
            
            if not results:
                print(f"❌ No contacts found matching '{search_term}'")
            else:
                print(f"\n✅ Found {len(results)} contact(s):")
                for idx, contact in enumerate(results, 1):
                    print(f"  {idx}. {contact['name']} - {contact['phone']}")
                    if contact['email']:
                        print(f"     Email: {contact['email']}")
                    if contact['address']:
                        print(f"     Address: {contact['address']}")
        
        elif choice == '4':
            print("\n✏️ UPDATE CONTACT")
            print("-"*40)
            search_term = get_input("Enter name or phone number to find contact", required=True)
            contact_book.update_contact(search_term)
        
        elif choice == '5':
            print("\n❌ DELETE CONTACT")
            print("-"*40)
            search_term = get_input("Enter name or phone number to find contact", required=True)
            contact_book.delete_contact(search_term)
        
        elif choice == '6':
            print("\n" + "="*60)
            print("🙏 Thank you for using Unique Contact Book!")
            print("Your contacts are saved safely. Goodbye! 👋")
            print("="*60)
            break
        
        else:
            print("\n❌ Invalid choice. Please enter a number between 1 and 6.")


if __name__ == "__main__":
    main()
