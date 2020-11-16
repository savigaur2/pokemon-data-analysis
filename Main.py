##############################################################################################################
#    Name: Savishwa Gaur
#    Poject Description: Answer the question "Do later generations produce stronger Pokemon?"
#                        I will be predicting the generation of pokemon based on their stats, number of
#                        abilities and catch rate. The analysis will be considering the following categories:
#                        Strongest Overall, Fastest, Most Defensive, Hardest Hitting, Hardest to Obtain.
#                        Rondom forest will be used to model the data
##############################################################################################################
def Function():
    import pandas as pd
    from sklearn.ensemble import RandomForestRegressor
    from sklearn.model_selection import train_test_split
    from sklearn.metrics import mean_absolute_error
    print('Import sucessful')

    # Read data
    file_path = "Data/pokedex_(Update_05.20).csv"
    pokemon_data = pd.read_csv(file_path)
    print('Data has been read sucessfully')

    # Filter the data set of null values
    features = ['total_points', 'catch_rate', 'abilities_number']
    filtered_pokemon_data = pokemon_data.dropna(subset = features)
    print('Data has been filtered sucessfully')

    # Sort the data set based on Base stats
    filtered_pokemon_data = filtered_pokemon_data.sort_values('total_points', ascending = False)
    print('Data sucessfully sorted based on total_points')

    # Define out target(y) and our features
    y = filtered_pokemon_data.generation
    X = filtered_pokemon_data[features]

    # Split our data into training and validation sets
    train_X, val_X, train_y, val_y = train_test_split(X, y, random_state = 0)

    # Define model as Random Forest
    pokemon_model = RandomForestRegressor(random_state = 1)

    # Fit the data to our training data
    pokemon_model.fit(train_X, train_y)

    # Make a prediction on the generation with our validation data
    generation_preditions = pokemon_model.predict(val_X)

    # Truncate the values in the predictions so that they are whole numbers
    for i in range(len(generation_preditions)):
        generation_preditions[i] = int(generation_preditions[i])

    print()
    print('Generation Predictions: ')
    print(generation_preditions)

    # Now that we have the predictions, examine the data using numpy
    import numpy as np
    mean = np.mean(generation_preditions)
    varianve = np.var(generation_preditions)
    std = np.std(generation_preditions)
    print()
    print('Stats for the predictions:')
    print('------------------------------------------------------')
    print('| Mean |       Variance       |  Standard Deviation  |')
    print('------------------------------------------------------')
    print('|', mean, ' | ', varianve, ' | ', std, ' |')
    print('------------------------------------------------------')

    # Validate the accuracy of the model
    print()
    print('Model Validation:')
    print('------------------------------------------------------')
    print('|                 Mean Absolute Error                |')
    print('------------------------------------------------------')
    print('|                 ', mean_absolute_error(val_y, generation_preditions), '                 |')
    print('------------------------------------------------------')

    return generation_preditions

def Predictio_toString():
    str_return = "["
    row_count = 0
    gen = Function()
    for i in gen:
        if row_count == 21:
            str_return = str_return + '\n'
            row_count = 0
        str_return = str_return + str(i) + " "
        row_count = row_count + 1
    str_return = str_return + "]"
    return str_return

# Fuction for writing to the HTML file we want to display using BeautifulSoup
def Write_to_HTML(str_html_tag, str_data):
    import bs4
    # Load file
    with open("templates/index.html") as file_IN:
        index = file_IN.read()
        soup = bs4.BeautifulSoup(index, features = "lxml")

    # Navigate to specific html body element
    soup.body.append(str_data)

    # Save the file again
    with open("templates/index.html", "w") as file_OUT:
        file_OUT.write(str(soup))

    return file_OUT
