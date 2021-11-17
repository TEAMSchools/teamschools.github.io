# Documentation

This site is hosted on GitHub Pages and built by Jupyter-Book. You can create new pages by writing them out in Markdown or Jupyter notebook. When the updated repository is approved and merged to the main branch in GitHub, a GitHub action runs the python command that rebuilds the site with your edits.

## Contributing and Editing Content

### GitHub Repository

Clone the [teamschools.github.io](https://github.com/TEAMSchools/teamschools.github.io) repository to your local machine.

Create a new branch for your changes.

Open the repository in VS Code or another text editor.

Open a pull request.

### Adding your content

Site content files are stored in ```teamschools.github.io/ktafdata/content```.
    
![](images/doc_1.png) 

Select (or create) a folder for your content and create a markdown file for your new page. Or copy the markdown documentation doc in the content/processes/documentation folder to not start from a blank slate.

Asterisks (*) add a bulleted (unordered) list

* Bulleted list example

Numbers add an ordered list, but won't automatically update like an outline.

1. Numbered list example

### Links

```[Brackets](link_or_path)``` makes a hyperlink in Markdown.

[Hyperlink example](https://www.youtube.com/watch?v=dQw4w9WgXcQ)

![](images/doc_4.png) 

### Adding images

Best practice is to make an 'images' subfolder and link to images/[name_of_file] with ![] before the path, so that you don't have to edit all the image links if your content folder moves elsewhere.

```![](link_to_image)``` inserts an image.

![](images/doc_3.png) 

### Formatting

Number of hash marks placed before text determine heading level (1 - 6), and puts headings in the sidebar navigation.

```# [space] Header Text```

![](images/doc_2.png) 



