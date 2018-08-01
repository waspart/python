import requests
import json
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS


url = "https://api.github.com/search/repositories?q=language:python&sort=stars"
ret = requests.get(url)
print("status code:", ret.status_code)
response_dict = ret.json()


print("Total repositories:", response_dict['total_count'])

repo_dicts = response_dict['items']
print('respositories returned: ', len(repo_dicts))
# print(response_dict.keys())
# print(response_dict.values())

# repo_dict = repo_dicts[0]
# print("\nkeys:", len(repo_dict))
# for key in sorted(repo_dict.keys()):
#     print(key)


# print("\nSelect information about first repository:")
# print("name:", repo_dict['name'])
# print("owner:", repo_dict['owner']['login'])
# print("stars:", repo_dict['stargazers_count'])
# print("repository:", repo_dict['html_url'])
# print("created:", repo_dict['created_at'])
# print("updated:", repo_dict['updated_at'])
# print("description:", repo_dict['description'])


names, stars = [], []
print("\nSelect information about each repository:")
for repo_dict in repo_dicts:
    # print("\nname:", repo_dict['name'])
    # print("owner:", repo_dict['owner']['login'])
    # print("stars:", repo_dict['stargazers_count'])
    # print("repository:", repo_dict['html_url'])
    # print("created:", repo_dict['created_at'])
    # print("updated:", repo_dict['updated_at'])
    # print("description:", repo_dict['description'])
    names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])

my_style = LS('#333366', base_style=LCS)
my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.title_font_size = 24
my_config.label_font_size = 14
my_config.major_label_font_size = 18
my_config.trunctate_label = 15
my_config.show_y_guides = False
my_config.width = 1000
chart = pygal.Bar(my_config, style=my_style)
chart.title = 'MOST-STARRED PYTHON PROJECTIONS ON GITHUB'
chart.x_labels = names
chart.add('stars', stars)
chart.render_to_file('python_repos.svg')

