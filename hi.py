import pandas as pd

data = {
    "State": [
        "Andhra Pradesh",
        "Arunachal Pradesh",
        "Assam",
        "Bihar",
        # ... Add more states ...
    ],
    "Capital": [
        "Amaravati",
        "Itanagar",
        "Dispur",
        "Patna",
        # ... Add more capitals ...
    ],
    "Population (2021)": [
        53903393,
        1570458,
        35607039,
        124799926,
        # ... Add more populations ...
    ],
    "Area (sq km)": [
        160205,
        83743,
        78438,
        94163,
        # ... Add more areas ...
    ],
    # Add more data columns for other information you need.
}

df = pd.DataFrame(data)

# Save the dataset to a CSV file
df.to_csv("indian_states_dataset.csv", index=False)
