def sandwich_ingredients(*args):
    """Print a summary of sandwich ingredients being ordered."""
    print("\nThese are the sandwich ingredients:")
    for arg in args:
        print(f"- {arg}")

sandwich_ingredients()
sandwich_ingredients('lettuce', 'cucumber', 'chicken')
sandwich_ingredients('lettuce', 'cucumber', 'pastrami', 'tuna')
