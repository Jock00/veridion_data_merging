from merge_data import merge_facebook_google, merge_final_website
from read_data import get_data, get_data_website
from write_data import extract_data_to_csv

if __name__ == "__main__":
    folder_input_location = "../data/input/"
    folder_output_location = "../data/output/final/"
    output_file = "output.csv"
    files = {
        "google": folder_input_location + 'google_dataset.csv',
        "facebook": folder_input_location + 'facebook_dataset.csv',
        "website": folder_input_location + 'website_dataset.csv',
    }
    print(f"Loading data from {folder_input_location}")

    print("Reading website data ..")
    website = get_data_website(files["website"])
    print("Done!")

    print("Reading google data ..")
    google = get_data(files["google"])
    print("Done!")

    print("Reading facebook data ..")
    facebook = get_data(files["facebook"])
    print("Done!")

    print("Merging facebook and google data ..")
    merged_data = merge_facebook_google(facebook, google)
    print("Done!")

    print("Merging with website data ..")
    final_data = merge_final_website(merged_data, website)
    print("Done!")

    print("Converting data to CSV")
    extract_data_to_csv(final_data, folder_output_location + output_file)
    print(f"Done! Data is saved at {folder_input_location}{output_file}")

