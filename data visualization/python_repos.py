import requests

# 执行API调用并存储响应
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url, verify=False)
print("Status code:", r.status_code)

# 将API响应存储在一个变量中
response_dict = r.json()

# 处理结果
print("Total repositories returned:", response_dict['total_count'])

# 探索有关仓库的信息
repo_dicts = response_dict['items']
print("Repositories returned:", len(repo_dicts))


print("\nSelected information about every repository:")
for repo_dict in repo_dicts:
    print("\nName:", repo_dict['name'])
    print("Owner:", repo_dict['owner']['login'])
    print("Stars", repo_dict['stargazers_count'])
    print("Repository:", repo_dict['html_url'])
    print("Created:", repo_dict['created_at'])
    print("Updated:", repo_dict['updated_at'])
    print("Description:", repo_dict['description'])


# print("\nKeys:", len(repo_dict))
# for key in sorted(repo_dict.keys()):
#     print(key)
