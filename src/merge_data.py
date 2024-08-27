def merge_facebook_google(facebook, google):
    final_data = {}

    for key in set(facebook).union(google):  # Union of keys from both dicts
        if key in facebook and key in google:
            # Both dictionaries have this key
            final_data[key] = {}
            for region in set(facebook[key]).union(google[key]):
                if region in facebook[key] and region in google[key]:
                    # Both dictionaries have this region
                    final_data[key][region] = {}
                    for country in set(
                            facebook[key][region]).union(google[key][region]):
                        if (country in facebook[key][region] and \
                                country in google[key][region]):
                            # Merge data for the same country
                            merged_country_data = \
                                google[key][region][country] + \
                                facebook[key][region][country]
                            final_data[key][region][
                                country] = merged_country_data
                        else:
                            # If country is only in one dictionary, take it as is
                            final_data[key][region][country] = \
                                facebook[key][region].get(
                                    country, google[key][region].get(country))
                else:
                    # If region is only in one dictionary, take it as is
                    final_data[key][region] = facebook[key].get(
                        region, google[key].get(region))
        else:
            # If key is only in one dictionary, take it as is
            final_data[key] = facebook.get(key, google.get(key))

    return final_data


def merge_final_website(final, website):
    result = {}
    for site, data in final.items():
        if site in website:
            result[website[site]] = final[site]
    return result
