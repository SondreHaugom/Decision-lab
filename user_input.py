def user_input():
    try:
        user_input = input("You: ")
    except Exception as e:
        print(f"Error: {e}")