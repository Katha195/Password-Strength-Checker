import re
import math

def check_password_strength(password):

    score = 0
    feedback = []

    length = len(password)
    if length < 6:
        feedback.append("❌ Too short! Use at least 8 characters")
    elif length < 8:
        score += 1
        feedback.append("⚠️  Increase length to at least 8 characters")
    elif length < 12:
        score += 2
        feedback.append("✓ Good length, but 12+ is better")
    else:
        score += 3
        feedback.append("✓ Excellent length!")
    
    # Character variety checks
    has_lower = bool(re.search(r'[a-z]', password))
    has_upper = bool(re.search(r'[A-Z]', password))
    has_digit = bool(re.search(r'\d', password))
    has_special = bool(re.search(r'[!@#$%^&*()_+\-=\[\]{};:\'",.<>?/\\|`~]', password))
    
    if has_lower:
        score += 1
        feedback.append("✓ Contains lowercase letters")
    else:
        feedback.append("❌ Add lowercase letters (a-z)")
    
    if has_upper:
        score += 1
        feedback.append("✓ Contains uppercase letters")
    else:
        feedback.append("❌ Add uppercase letters (A-Z)")
    
    if has_digit:
        score += 1
        feedback.append("✓ Contains numbers")
    else:
        feedback.append("❌ Add numbers (0-9)")
    
    if has_special:
        score += 2
        feedback.append("✓ Contains special characters")
    else:
        feedback.append("❌ Add special characters (!@#$%^&*)")
    
    common_patterns = [
        r'123', r'abc', r'password', r'qwerty', 
        r'admin', r'letmein', r'welcome', r'monkey'
    ]
    
    has_common = any(re.search(pattern, password.lower()) for pattern in common_patterns)
    if has_common:
        score -= 2
        feedback.append("⚠️  Contains common patterns - avoid predictable sequences")
    else:
        score += 1
        feedback.append("✓ No common patterns detected")
    
    if re.search(r'(.)\1{2,}', password):
        score -= 1
        feedback.append("⚠️  Avoid repeating characters (e.g., 'aaa')")

    charset_size = 0
    if has_lower: charset_size += 26
    if has_upper: charset_size += 26
    if has_digit: charset_size += 10
    if has_special: charset_size += 32
    
    entropy = length * math.log2(charset_size) if charset_size > 0 else 0
    
    if score <= 3:
        strength = "VERY WEAK 🔴"
        color = "\033[91m"  # Red
    elif score <= 5:
        strength = "WEAK 🟠"
        color = "\033[93m"  # Yellow
    elif score <= 7:
        strength = "MODERATE 🟡"
        color = "\033[93m"  # Yellow
    elif score <= 9:
        strength = "STRONG 🟢"
        color = "\033[92m"  # Green
    else:
        strength = "VERY STRONG 🟢"
        color = "\033[92m"  # Green
    
    reset_color = "\033[0m"

    if entropy < 28:
        crack_time = "Less than 1 second"
    elif entropy < 36:
        crack_time = "Few seconds to minutes"
    elif entropy < 60:
        crack_time = "Hours to days"
    elif entropy < 80:
        crack_time = "Months to years"
    else:
        crack_time = "Centuries+"
    
    return {
        'score': score,
        'strength': strength,
        'color': color,
        'reset': reset_color,
        'feedback': feedback,
        'entropy': entropy,
        'crack_time': crack_time,
        'length': length
    }


def display_results(result):
    """Display password strength analysis in a formatted way"""
    
    print("\n" + "="*60)
    print(f"{result['color']}PASSWORD STRENGTH: {result['strength']}{result['reset']}")
    print("="*60)
    print(f"Score: {result['score']}/10")
    print(f"Length: {result['length']} characters")
    print(f"Entropy: {result['entropy']:.1f} bits")
    print(f"Estimated crack time: {result['crack_time']}")
    print("\n" + "-"*60)
    print("FEEDBACK:")
    print("-"*60)
    for item in result['feedback']:
        print(f"  {item}")
    print("="*60 + "\n")


def main():
    """Main function to run the password strength checker"""
    
    print("\n" + "="*60)
    print("🔒 PASSWORD STRENGTH CHECKER 🔒")
    print("="*60)
    print("Tips for strong passwords:")
    print("  • Use at least 12 characters")
    print("  • Mix uppercase, lowercase, numbers, and symbols")
    print("  • Avoid common words and patterns")
    print("  • Use unique passwords for each account")
    print("="*60 + "\n")
    
    while True:
        password = input("Enter password to check (or 'quit' to exit): ")
        
        if password.lower() == 'quit':
            print("\nStay secure! 👋\n")
            break
        
        if not password:
            print("Please enter a password.\n")
            continue
        
        result = check_password_strength(password)
        display_results(result)


if __name__ == "__main__":
    main()
