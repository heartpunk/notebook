import codecs
import markdown
import glob



def index(base_dir='./'):
    return markdown.markdown(
        "## daily notes\n\n%s" % "\n".join(['- [%s](%shtml)' % (name[8:-3], name[:-2])
                                            for name in glob.glob(base_dir + 'daily/*.md')]))

def write_index(output_path='./index.html', base_dir=None):
    with codecs.open(output_path, mode='w', encoding='utf-8') as output:
        output.write(index(base_dir) if base_dir else index())

def write_html(glob_pattern="**/*.md"):
    for path in glob.glob(glob_pattern):
        with codecs.open(path, mode='r', encoding='utf-8') as markdown_file:
            with codecs.open("%shtml" % path[:-2], mode='w', encoding='utf-8') as html_file:
                html_file.write(markdown.markdown(markdown_file.read()))


if __name__ == "__main__":
    write_index()
    write_html()
