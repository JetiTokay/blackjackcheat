# a Blackjack strategy guide to help players decide their next move based on their hand. There are a few things to tweak to make it work better:
def display_menu():
    print("\n\033[1;32m=====================")  # Green for the menu header
    print("  🃏 \033[1;34mBlackjack Helper \033[1;32m🃏")  # Blue for "Blackjack Helper"
    print("=====================\033[0m")  # Reset color
    print("\033[1;33m1. Enter Cards\033[0m")  # Yellow for option 1
    print("\033[1;31m2. Exit\033[0m")  # Red for option 2
    print("=====================\033[0m")  # Reset color

def blackjack_strategy():
    while True:
        # Main menu display
        display_menu()
        
        # Get player choice
        choice = input("\033[1;36mChoose an option (1 or 2): \033[0m")  # Cyan for prompt
        
        if choice == '1':
            print('\n\033[1;35mEnter your cards (e.g., "A 6", "A 8", "A 9"): \033[0m')  # Magenta for input prompt
            cards = input().strip().upper()

            # Handling pairs
            if cards in ['A A', '8 8']:
                print('\033[1;33mSplit\033[0m')  # Yellow for "Split"
            elif cards == '10 10':
                print("\033[1;33mDon't split\033[0m")  # Yellow for "Don't split"
            elif cards == '9 9':
                print('\033[1;34mSplit against 2-9, except for 7. Otherwise, STAND\033[0m')  # Blue for strategy
            elif cards == '4 4':
                print('\033[1;34mSplit against 5 & 6, otherwise HIT\033[0m')
            elif cards == '2 2':
                print('\033[1;34mSplit against 2-7, otherwise HIT\033[0m')

            # Hard totals
            elif cards == '16':
                print('\033[1;31mSurrender against 9-A, otherwise HIT\033[0m')  # Red for surrender
            elif cards == '15':
                print('\033[1;31mSurrender against 10, otherwise HIT\033[0m')
            elif cards in ['17', '18', '19', '20', '21']:
                print('\033[1;32mSTAND\033[0m')  # Green for STAND
            elif cards in ['13', '14', '15', '16']:
                print('\033[1;33mStand against 2-6, HIT against 7-A\033[0m')  # Yellow for strategy
            elif cards == '12':
                print('\033[1;33mStand against 4-6, HIT against everything else\033[0m')
            elif cards == '11':
                print('\033[1;32mDouble Down\033[0m')  # Green for Double Down
            elif cards == '10':
                print('\033[1;32mDouble against 2-9, otherwise HIT\033[0m')
            elif cards == '9':
                print('\033[1;32mDouble against 3-6, otherwise HIT\033[0m')
            elif cards in ['8', '7', '6', '5', '4', '3', '2']:
                print('\033[1;31mHIT\033[0m')  # Red for HIT

            # Soft hands (Aces counted as 11)
            elif cards in ['A 8', 'A 9']:
                print('\033[1;32mSTAND\033[0m')  # Green for STAND
            elif cards == 'A 7':
                print('\033[1;32mDouble against 2-6, Stand against 7-8, HIT against 9-A\033[0m')
            elif cards in ['A 6', 'A 5']:
                print('\033[1;32mDouble against 3-6, otherwise HIT\033[0m')
            elif cards in ['A 4', 'A 3']:
                print('\033[1;32mDouble against 4-6, otherwise HIT\033[0m')
            elif cards in ['A 2']:
                print('\033[1;32mDouble against 5-6, otherwise HIT\033[0m')

            else:
                print('\033[1;31mInvalid input, try again.\033[0m')  # Red for invalid input
        
        elif choice == '2':
            print("\n\033[1;35mThanks for using Blackjack Helper! 🎲\033[0m")  # Magenta for goodbye message
            break
        
        else:
            print("\033[1;31mInvalid option, please choose 1 or 2.\033[0m")  # Red for invalid option

# Start the game
blackjack_strategy()
