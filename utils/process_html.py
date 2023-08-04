from typing import List
from bs4 import BeautifulSoup
import time

# with open('/Users/robincahierre/Desktop/aws_home_page.html', 'r') as f_:
#     print(f"NUMBER OF WORDS: {len(f_.read().split())}\n")

html_file_path = '/Users/robincahierre/Desktop/aws_home_page.html'
output_file_path = '/Users/robincahierre/Desktop/aws_home_page_cleaned.html'

def load_soup(file_path: str) -> BeautifulSoup:
    with open(file_path, 'r') as file_:
        return BeautifulSoup(file_, 'lxml')


def remove_tags(soup: BeautifulSoup, tags_to_remove: List[str]) -> BeautifulSoup:
    for tag_name in tags_to_remove:
        for tag in soup.find_all(tag_name):
            tag.decompose()
    return soup


soup = load_soup(html_file_path)

print(f"LENGTH OF THE SOUP: {len(soup.prettify().split())}\n")

soup = remove_tags(soup, ['meta', 'script', 'style', 'svg', 'iframe'])
print(f"LENGTH OF THE SOUP: {len(soup.prettify().split())}\n")

# print(soup.current_data)
# time.sleep(10)
print(f"CURRENT SOUP BODY'S CHILDREN LEN: {len(soup.body.contents)}\n")

# for child_tag in soup.body.contents:
#     print(f"TAG: {child_tag.name}")
#     print(f"NUMBER OF 'WORDS': {len(child_tag.text.split())}")
#     if child_tag.name is None:
#         print("CHILD TAG")
#         print(child_tag)
#         # print(child_tag.contents)
#         print("**********************************************\n\n\n")
#         time.sleep(10)
#     print("\n")

for child in soup.body.children:
    print("CHILD LEVEL 1")
    if child.name:
        print(child.name)
        print(child.attrs)
        for ch in child.children:
            if ch.name:
                print("CHILD LEVEL 2")
                print(ch.name)
                print(ch.attrs)
                print(f"LENGTH OF CHILD: {len(str(ch).split())}")
    else:
        ### NAVIGABLE STRING
        if not str(child.string).strip():
            print("EMPTY NAVIGABLE STRING!")
        else:
            print(f"CHILD STRING: {child.string}\n")
        #print(str(child.string))
        # print()
    print("\n"*2)

# print(f"CURRENT SOUP BODY'S CHILDREN LEN: {len(soup.body.contents)}\n")

    # print(f"INITIAL SOUP LENGHT: {len(soup.prettify().split())}\n")
    # script_tags = soup.find_all('script')
    # print(f"NUMBER OF SCRIPT TAGS: {len(script_tags)}\n")
    # style_tags = soup.find_all('style')
    # print(f"NUMBER OF STYLE TAGS: {len(style_tags)}\n")
    
    # svg_tags = soup.find_all('svg')
    # print(f"NUMBER OF SVG TAGS: {len(svg_tags)}\n")

    # meta_tags = soup.find_all('meta')
    # print(f"NUMBER OF META TAGS: {len(meta_tags)}\n")


    # print("REMOVING THE SCRIPT TAGS\n")
    # for script_tag in script_tags: #soup.find_all('script'):
    #     script_tag.decompose() # remove the tag

    # # Print the soup to verify that script tags have been removed
    # #print(soup.prettify())
    # print(f"LENGTH OF THE SOUP: {len(soup.prettify().split())}\n")

    # print("REMOVING THE STYLE TAGS\n")
    # for style_tag in style_tags: #soup.find_all('script'):
    #     style_tag.decompose() # remove the tag

    # print(f"LENGTH OF THE SOUP: {len(soup.prettify().split())}\n")

    # print("REMOVING THE SVG TAGS\n")
    # for svg_tag in svg_tags:
    #     svg_tag.decompose() # remove the tag

    # print(f"LENGTH OF THE SOUP: {len(soup.prettify().split())}\n")

    # print("REMOVING THE META TAGS\n")
    # for meta_tag in meta_tags:
    #     meta_tag.decompose() # remove the tag

    # print(f"LENGTH OF THE SOUP: {len(soup.prettify().split())}\n")

    # with open(output_file_path, 'w') as output_:
    #     output_.write(soup.prettify())
