import streamlit as st

# Set page title
st.title(":blue[Café ] :red[Boulangerie]")

# Custom CSS for column width
st.markdown("""
    <style>
        div[data-testid="stColumn"] {
            width: fit-content !important;
            flex: unset;
        }
        div[data-testid="stColumn"] * {
            width: fit-content !important;
        }
    </style>
    """, unsafe_allow_html=True)

# Function to display a food item with a counter
def food(name, description, food, price):
    st.subheader(f"{name}: ${price}")

    col14, col15 = st.columns(2)

    # Initialize the counter for this specific food item
    if 'counters' not in st.session_state:
        st.session_state.counters = {}

    if name not in st.session_state.counters:
        st.session_state.counters[name] = 0

    with col14:
        # Button to increment the counter for this specific food item
        if st.button(f"➕ {name}"):
            st.session_state.counters[name] += 1

    with col15:
        # Button to decrement the counter for this specific food item
        if st.button(f"➖ {name}"):
            if st.session_state.counters[name] > 0:
                st.session_state.counters[name] -= 1
            else:
                st.warning(f"You can't order less than 0 {name}s!")  # Warn if trying to go below 0

    # Display the counter for this specific food item
    counter = st.session_state.counters[name]
    if counter == 1:
        st.write(f"You've ordered {counter} {name}")
    elif counter > 1:
        st.write(f"You've ordered {counter} {name}s")

# Function to calculate and display the total cost
def calculate_total_cost():
    # Define the prices for each food item
    food_prices = {
        "Chocolate Chip Cookie": 1.99,
        "Maple Glazed Donut": 1.99,
        "Tiramisu": 3.99,
        "Cinnamon Sugar Beavertail": 4.99
    }

    # Calculate the subtotal
    subtotal = 0
    for name, counter in st.session_state.counters.items():
        if name in food_prices:
            subtotal += counter * food_prices[name]

    # Calculate the tax (13% for Ontario, Canada)
    tax_rate = 0.13
    tax = subtotal * tax_rate

    # Calculate the total cost
    total_cost = subtotal + tax

    # Display the subtotal, tax, and total cost
    st.write("---")
    st.write(f"### Subtotal: ${subtotal:.2f}")
    st.write(f"### Tax (13%): ${tax:.2f}")
    st.write(f"### Total Cost: ${total_cost:.2f}")

# Display food items
food("Chocolate Chip Cookie", "description", "food", "1.99")
st.image("Tasty101ChocChipCookiesYTUPLOADFINAL.jpg")
st.write("Ingredients: Brown sugar, Salt, Unsalted butter, Egg, Vanilla extract, All-purpose flour, Baking soda, milk or semi-sweet chocolate chunks, Dark chocolate chunks.")

food("Maple Glazed Donut", "description", "food", "1.99")
st.image("maple-icing-for-donuts-min.jpg")
st.write("Ingredients: Whole Milk, Active Dry Yeast, Granulated Sugar, Eggs, Unsalted Butter, Vanilla Extract, Salt, Freshly Grated Nutmeg, Ground Cinnamon, Bread Flour, Powdered Sugar, Maple Syrup, Maple Extract.")

food("Tiramisu", "description", "food", "3.99")
st.image("best-tiramisu-recipe-1-of-1.jpg")
st.write("Ingredients: Strong Brewed Coffee, Lady Finger Biscuits, Mascarpone Cheese, Whipped Cream, Sugar, Vanilla Extract, Cocoa, Chocolate.")

food("Cinnamon Sugar Beavertail", "description", "food", "4.99")
st.image("cinnamon-sugar-beaver-tails-4.jpg")
st.write("Ingredients: Water, Active Dry Yeast, White Sugar, Warm Milk, Salt, Vanilla Extract, Eggs, Canola Oil, All Purpose Flour, Ground Cinnamon.")

# Display the logo
st.logo("Screenshot 2025-03-01 145811.png")

# Calculate and display the total cost
calculate_total_cost()