import streamlit as st
st.title(":blue[Costco] :red[Food court]")
col1, col2, col3,= st.columns(3)
col4, col5, col6,= st.columns(3)
col7, col8, col9,= st.columns(3)
col10, col11, col12,= st.columns(3)
col13, col14, col15,= st.columns(3)







sentiment_mapping = ["one", "two", "three", "four", "five"]

with col1:
    st.subheader("Chicken bake")
    st.image("C:/Users/kai_k/OneDrive/Pictures/bake8.jpg")
    st.write("$3.99: Chicken breast, Cheese, Bacon, Caesar Dressing.")

    selected = st.feedback("stars", key="chicken_bake")
    if selected is not None:  # Ensure a selection was made
        rating_text = f"You rated the Chicken Bake {sentiment_mapping[selected]} star."
        
        if selected > 0:  # Fix: Allow "0" (1 star) to work
            rating_text = f"You rated the Chicken Bake {sentiment_mapping[selected]} stars."

        st.markdown(rating_text)  # Display the rating

        st.subheader("Chicken Bake: $3.99")




        




with col2:
    st.subheader("Hot dog & Soda")
    st.image("C:/Users/kai_k/OneDrive/Pictures/Costco-Hot-Dog-1.50-food-court-2024-03-14T140356Z_703008482_MT1USATODAY22769146_RTRMADP_3_THIS-HOT-DOG-AND-DRINK-COMBO-IS-SINGLE-HANDEDLY-THE-MOST.webp")
    st.write("$1.50: All beef hot dog and 20 oz soda (with refill).")


    selected = st.feedback("stars", key="hot_dog")
    if selected is not None:  # Ensure a selection was made
        rating_text = f"You rated the Hot Dog {sentiment_mapping[selected]} star."
        
        if selected > 0:  # Fix: Allow "0" (1 star) to work
            rating_text = f"You rated the Hot Dog {sentiment_mapping[selected]} stars."

        st.markdown(rating_text)  # Display the rating


with col3:
    st.subheader("Pepperoni Pizza")
    st.image("C:/Users/kai_k/OneDrive/Pictures/Costco-food-court-pizza.webp")
    st.write("$1.99 per slice, 9.95 18 inch whole.")


    



    selected = st.feedback("stars", key="pepperoni_pizza")
    if selected is not None:  # Ensure a selection was made
        rating_text = f"You rated the Pepperoni Pizza {sentiment_mapping[selected]} star."
        
        if selected > 0:  # Fix: Allow "0" (1 star) to work
            rating_text = f"You rated the Pepperoni Pizza {sentiment_mapping[selected]} stars."

        st.markdown(rating_text)  # Display the rating


with col4:
    st.subheader("Cheese Pizza")
    st.image("C:/Users/kai_k/OneDrive/Pictures/hawaii-america-jan-2013-scaled.jpg")
    st.write("$1.99 per slice, 9.95 18 inch whole.")



    selected = st.feedback("stars", key="Cheese_pizza")
    if selected is not None:  # Ensure a selection was made
        rating_text = f"You rated the Cheese pizza {sentiment_mapping[selected]} star."
        
        if selected > 0:  # Fix: Allow "0" (1 star) to work
            rating_text = f"You rated the Cheese pizza {sentiment_mapping[selected]} stars."

        st.markdown(rating_text)  # Display the rating

with col5:
    st.subheader("Chicken & bacon Sandwich")
    st.image("C:/Users/kai_k/OneDrive/Pictures/Costco-ChickenBacon-1.webp")
    st.write("$6.99: sliced chicken breast, cheddar cheese, bacon jam, mayo/mustard blend.")



    selected = st.feedback("stars", key="chicken_bacon")
    if selected is not None:  # Ensure a selection was made
        rating_text = f"You rated the Chicken & bacon sandwich {sentiment_mapping[selected]} star."
        
        if selected > 0:  # Fix: Allow "0" (1 star) to work
            rating_text = f"You rated the Chicken & bacon sandwich {sentiment_mapping[selected]} stars."

        st.markdown(rating_text)  # Display the rating



with col6:
    st.subheader("Rotisserie Chicken Caesar Salad")
    st.image("C:/Users/kai_k/OneDrive/Pictures/costco-food-court-rotisserie-chicken-caesar-salad.jpg")
    st.write("$6.99: rotisserie chicken breast, Romaine, parmesan cheese, caesar dressing.")


    selected = st.feedback("stars", key="Rotisserie_Chicken_Caesar_Salad")
    if selected is not None:  # Ensure a selection was made
        rating_text = f"You rated the Rotisserie Chicken Caesar Salad {sentiment_mapping[selected]} star."
        
        if selected > 0:  # Fix: Allow "0" (1 star) to work
            rating_text = f"You rated the Rotisserie Chicken Caesar Salad {sentiment_mapping[selected]} stars."

        st.markdown(rating_text)  # Display the rating






with col7:
    st.subheader("Double chunk chocolate cookie")
    st.image("C:/Users/kai_k/OneDrive/Pictures/2024-0729-costco-cookie-03a-1600w.jpg")
    st.write("$2.49: chocolate, butter and served warm.")


    selected = st.feedback("stars", key="Double_chunk_chocolate_cookie")
    if selected is not None:  # Ensure a selection was made
        rating_text = f"You rated the Double chunk chocolate cookie {sentiment_mapping[selected]} star."
        
        if selected > 0:  # Fix: Allow "0" (1 star) to work
            rating_text = f"You rated the Double chunk chocolate cookie {sentiment_mapping[selected]} stars."

        st.markdown(rating_text)  # Display the rating



with col8:
    st.subheader("Ice cream Sundae")
    st.image("C:/Users/kai_k/OneDrive/Pictures/Costco-Strawberry-Sundae-1024x689.jpg")
    st.write("$2.49: vanilla ice cream with strawberry or chocoklate topping.")


    selected = st.feedback("stars", key="Ice_cream_Sundae")
    if selected is not None:  # Ensure a selection was made
        rating_text = f"You rated the Ice cream Sundae {sentiment_mapping[selected]} star."
        
        if selected > 0:  # Fix: Allow "0" (1 star) to work
            rating_text = f"You rated the Ice cream Sundae {sentiment_mapping[selected]} stars."

        st.markdown(rating_text)  # Display the rating
    

with col9:
    st.subheader("Ice cream cup")
    st.image("C:/Users/kai_k/OneDrive/Pictures/5-chocolate-ice-cream-cup-1720553841.jpg")
    st.write("$1.99: vanilla ice cream, strawberry ice cream.")



    selected = st.feedback("stars", key="Ice_cream_cup")
    if selected is not None:  # Ensure a selection was made
        rating_text = f"You rated the Ice cream cup {sentiment_mapping[selected]} star."
        
        if selected > 0:  # Fix: Allow "0" (1 star) to work
            rating_text = f"You rated the Ice cream cup {sentiment_mapping[selected]} stars."

        st.markdown(rating_text)  # Display the rating



with col10:
    st.subheader("Berry smoothie")
    st.image("C:/Users/kai_k/Downloads/Costco-Fruit-Smoothie-1024x689.jpg")
    st.write("$2.99: 4 servings of food, strawberry, blackberry, acai.")


    selected = st.feedback("stars", key="Berry_smoothie")
    if selected is not None:  # Ensure a selection was made
        rating_text = f"You rated the Berry smoothie {sentiment_mapping[selected]} star."
        
        if selected > 0:  # Fix: Allow "0" (1 star) to work
            rating_text = f"You rated the Berry smoothie {sentiment_mapping[selected]} stars."

        st.markdown(rating_text)  # Display the rating


with col11:
    st.subheader("Mango Smoothie")
    st.image("C:/Users/kai_k/OneDrive/Pictures/intro-1686773008.jpg")
    st.write("$2.99: 4 servings of fruit and mango.")


    selected = st.feedback("stars", key="Mango_Smoothie")
    if selected is not None:  # Ensure a selection was made
        rating_text = f"You rated the Mango Smoothie {sentiment_mapping[selected]} star."
        
        if selected > 0:  # Fix: Allow "0" (1 star) to work
            rating_text = f"You rated the Mango Smoothie {sentiment_mapping[selected]} stars."

        st.markdown(rating_text)  # Display the rating






with col12:
    st.subheader("Cold Brew Mocha Freeze")
    st.image("C:/Users/kai_k/OneDrive/Pictures/Costco-Cold-Brew-Mocha-Freeze.jpg")
    st.write("$2.99: cold brew ice coffee, kirkland colombian beans, premium chocolate.")
    


    selected = st.feedback("stars", key="Cold_Brew_Mocha_Freeze")
    if selected is not None:  # Ensure a selection was made
        rating_text = f"You rated the Cold Brew Mocha Freeze {sentiment_mapping[selected]} star."
        
        if selected > 0:  # Fix: Allow "0" (1 star) to work
            rating_text = f"You rated the Cold Brew Mocha Freeze {sentiment_mapping[selected]} stars."

        st.markdown(rating_text)  # Display the rating


    



with col13:
    st.subheader("Cold Brew Latte Freeze")
    st.image("C:/Users/kai_k/OneDrive/Pictures/cold-brew-latte-freeze-1657826796.jpg")
    st.write("$2.99: cold brew ice coffee, milk and sugar.")

    selected = st.feedback("stars", key="Cold_Brew_Latte_Freeze")
    if selected is not None:  # Ensure a selection was made
        rating_text = f"You rated the Cold Brew Latte Freeze {sentiment_mapping[selected]} star."
        
        if selected > 0:  # Fix: Allow "0" (1 star) to work
            rating_text = f"You rated the Cold Brew Latte Freeze {sentiment_mapping[selected]} stars."

        st.markdown(rating_text)  # Display the rating



# when button is pressed, you add 1 to Xa 

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


st.subheader("Hot Dog & Soda: $1.50")

col14, col15= st.columns(2)

if 'counter' not in st.session_state:
    st.session_state.counter = 0


with col14:
# Button to increment the counter
    if st.button("➕hot dog"):
        st.session_state.counter += 1
    # st.write(f"You've ordered {st.session_state.counter} chicken bakes")


with col15:
# Button to increment the counter
# st.session_state.counter = 0
    if st.button("➖hot dog"):
        st.session_state.counter -= 1
        # if st.session_state.counter == 0:
            
        # st.session_state.counter -= 1 # Now it's equal to -1

        if st.session_state.counter == -1:
            st.session_state.counter = st.session_state.counter + 1
            

if st.session_state.counter == 1:              
    st.write(f"You've ordered {st.session_state.counter} hot dog")

if st.session_state.counter > 1:
    st.write(f"You've ordered {st.session_state.counter} hot dogs")






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

# Example usage
food("pepperoni pizza", "description", "food", "1.99")
food("Cheese Pizza", "description", "food", "1.99")
food("Chicken & bacon Sandwich", "description", "food", "6.99")
food("Chicken caesar Salad", "description", "food", "6.99")
food("Double chunk chocolate cookie", "description", "food", "2.49")
food("Ice cream Sundae", "description", "food", "2.49")
food("Ice cream cup", "description", "food", "1.99")
food("Berry smoothie", "description", "food", "2.99")
food("Mango Smoothie", "description", "food", "2.99")
food("Cold Brew Mocha Freeze", "description", "food", "2.99")
food("Cold Brew Latte Freeze", "description", "food", "2.99")









