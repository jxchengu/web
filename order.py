import streamlit as st
st.title(":blue[Café ] :red[Boulangerie]")
col1, col2, col3,= st.columns(3)
col4, col5, col6,= st.columns(3)
col7, col8, col9,= st.columns(3)
col10, col11, col12,= st.columns(3)
col13, col14, col15,= st.columns(3)




add_selectbox = st.sidebar.selectbox(
    "How would you like to be contacted?",
    ("Email", "Home phone", "Mobile phone")
)

# Using "with" notation
with st.sidebar:
    add_radio = st.radio(
        "Choose a order method",
        ("Pick up", "deliver")
    )
if add_radio == "deliver":
    address = st.text_input("Please enter your address:")
    st.write(f"You're delivery will arrive at {address}.")

st.header("Welcome to the cafe boulangerie app!")
st.write("Since it's you just signed up on our app, you can have a free coffee, a tiramisu and one pastry of your choice.")
st.image("C:/Users/kai_k/OneDrive/Pictures/Screenshots/Screenshot 2025-03-21 200559.png")
st.write("Below is your barcode for your free food!")
st.image("C:/Users/kai_k/OneDrive/Pictures/linear.png")

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





#you add 1 to -1.

# 3.plurals
# 4.add red, minus blue


# create a border at 0
# when they are at 0, warn people that they can't.

# when it's at 0, it stop's minusing 1 from 0









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
        if st.button(f"➕{name}"):
            st.session_state.counters[name] += 1

    with col15:
        # Button to decrement the counter for this specific food item
        if st.button(f"➖{name}"):
            st.session_state.counters[name] -= 1
            if st.session_state.counters[name] < 0:
                st.session_state.counters[name] = 0

    # Display the counter for this specific food item
    counter = st.session_state.counters[name]
    if counter == 1:
        st.write(f"You've ordered {counter} {name}")
    elif counter > 1:
        st.write(f"You've ordered {counter} {name}s")





def calculate_total_cost():

    food_prices = {
        "Chocolate Chip Cookie": 1.99,
        "Maple Glazed Donut": 1.99,
        "Tiramisu": 3.99,
        "Cinnamon Sugar Beavertail": 3.99
    }

    subtotal = 0
    for name, counter in st.session_state.counters.items():
        if name in food_prices:
            subtotal += counter * food_prices[name]

 
    tax_rate = 0.13
    tax = subtotal * tax_rate

 
    total_cost = subtotal + tax

    st.write("---")
    st.write(f"### Subtotal: ${subtotal:.2f}")
    st.write(f"### Tax (13%): ${tax:.2f}")
    st.write(f"### Total Cost: ${total_cost:.2f}")



    
    import re

    # Payment method selection
    option = st.selectbox(
        "How would you like to pay?",
        ("Credit Card", "Debit Card", "Cash", "Gift Card", "Apple Pay", "E-Transfer", "Google Pay", "Digital Wallets"),
    )

    st.write("You selected:", option)

    # Conditional logic for Credit Card or Debit Card
    if option in ["Credit Card", "Debit Card"]:
        card_number = st.text_input("Enter your card number (format: XXXX-XXXX-XXXX-XXXX):")
        confirm_button = st.button("Confirm")

        if confirm_button:
            if re.match(r"^\d{4}-\d{4}-\d{4}-\d{4}$", card_number):
                st.success(f"Card number {card_number} has been confirmed.")
            else:
                st.error("Invalid card number format. Please use the format XXXX-XXXX-XXXX-XXXX.")

    if option in ["Google Pay"]:
        if st.button("Confirm"):
            st.write("You have sucessfully payed with Google Pay.")
            
        
        
    

food("Chocolate Chip Cookie", "description", "food", "1.99")
st.image("C:/Users/kai_k/OneDrive/Pictures/Tasty101ChocChipCookiesYTUPLOADFINAL.jpg")
st.write("At Cafe Boulangerie, for just $1.99, you can enjoy a large chocolate chip cookie that is warm and soft on the outside while maintaing a golden crispy edge. The cookie is buttery, chocolatey, rich and one bite is heaven for your tastebuds.")
st.caption("Ingredients: Brown sugar, Salt, Unsalted butter, Egg, Vanilla extract, All-purpose flour, Baking soda, milk or semi-sweet chocolate chunks, Dark chocolate chunks.")


food("Maple Glazed Donut", "description", "food", "1.99")
st.image("C:/Users/kai_k/Downloads/maple-icing-for-donuts-min.jpg")
st.write("Like our chocolate chip cookie, our signature Maple Glazed Donuts also cost $1.99 which is the signature pastry perfect by Richard Zhan. The Donut is freshly fried each more with care and then it's dipped in a rich and delicate maple syrup. One bite of our donut and you will feel like you're in heaven.")
st.caption("Ingredients: Whole Milk, Active Dry Yeast, Granulated Sugar, Eggs, Unsalted Butter, Vanilla Extract, Salt, Freshly Grated Nutmeg, Ground Cinnamon, Bread Flour, Powdered Sugar, Maple Syrup, Maple Extract. ")


food("Tiramisu", "description", "food", "3.99")
st.image("C:/Users/kai_k/OneDrive/Pictures/best-tiramisu-recipe-1-of-1.jpg")
st.write("Often for birthdays and special ocassions, most customers come to our bakery to order our award winning no bake tiramisu which costs $3.99. Our tiramisu is a cake like dessert that is creamy, velvety, light, fluffy, smooth, airy that anyone would crave for.")
st.caption("Ingredients: Strong Brewed Coffee, Lady Finger Biscuits, Mascarpone Cheese, Whipped Cream, Sugar, Vanilla Extract, Cocoa, Chocolate.")


food("Cinnamon Sugar Beavertail", "description", "food", "3.99")
st.image("C:/Users/kai_k/Downloads/cinnamon-sugar-beaver-tails-4.jpg")
st.write("One of the most popular items that cafe boulangerie offers is our signature $3.99 cinnamon sugar beavertails which is fried pastry dough covered with cinnamon and sugar. Our beavertails are fluffy and soft on inside while maintaing a cinnamony and sweet golden crispy skin. ")
st.caption("Ingredients: Water, Active Dry Yeast, White Sugar, Warm Milk, Salt, Vanilla Extract, Eggs, Canola Oil, All Purpose Flour, Ground Cinnamon.")



st.logo("C:/Users/kai_k/OneDrive/Pictures/Screenshot 2025-03-01 145811.png")



calculate_total_cost()

















