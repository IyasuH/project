import os
import pandas as pd
import command

json_files=['all_materials.json', 'cements.json']

# update the JSON files to updated vlaues
# delete the if the JSON files alreday exists
print("[INFO] Deleting all .JSON files inorder to update")
for json_file in json_files:
    if os.path.exists(json_file):
        command.run(['rm', json_file])

# then run to scrape the web and save the results as JSON file
# using command to run terminal command of doing that
print("[INFO] Regenerating .JSON files by scraping given spiders")
command.run(['scrapy', 'crawl', 'cements', '-o', 'cements.json'])
command.run(['scrapy', 'crawl', 'all_materials', '-o', 'all_materials.json'])

# then converting JSON file to CSV using pandas to read and convert
print("[INFO] Converting given .JSON files to .CSV files")
for json_file in json_files:
    df = pd.read_json(r'{}'.format(json_file))
    df.to_csv(r'{}.csv'.format(json_file[:-5]), index=None)
