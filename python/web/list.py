
import cgi
import glob
from html.parser import HTMLParser

from .index import capture_output


head = '<html>' \
       '<head>' \
       '    <title>Platform.sh Python service examples</title>' \
       '<style type="text/css">' \
       '    details {' \
       '        margin-top: 1em;' \
       '        border: 1px solid #aaa;' \
       '        border-radius: 4px;' \
       '        padding: 0.5em;' \
       '        width: 90%;' \
       '    }' \
       '' \
       '    summary {' \
       '        font-weight: bold;' \
       '        margin: -.5em -.5em 0;' \
       '        padding: .5em;' \
       '        }' \
       '' \
       '    details[open] {' \
       '        padding: .5em;' \
       '    }' \
       '' \
       '    details[open] summary {' \
       '        border-bottom: 1px solid #aaa;' \
       '        margin-bottom: .5em;' \
       '    }' \
       '' \
       '    table, table td, table th {' \
       '        border: 1px solid black;' \
       '    }' \
       '</style>' \
       '</head>'

parser = HTMLParser()
parser.feed(head)

files = glob.glob('../examples/*.py')
for filename in files:
    name = __file__
#     $source = highlight_file($filename, true);
    source = filename
    # output = capture_output(function, filename)
    output = lambda filename: capture_output(filename)

    body = '<body>' \
           '<h1>Service examples for Python' \
           '<details>' \
           '<summary>{} Sample Code</summary>' \
           '<section>' \
           '<h3>Source</h3>' \
           '{}' \
           '</section>' \
           '<section>' \
           '<h3>Output</h3' \
           '{}' \
           '</section>' \
           '</details>' \
           '</body>' \
           '</html>'.format(name, source, output)

    parser.feed(body)

# <body>
# <h1>Service examples for Python</h1>

# python
# files = glob.glob('../examples/*.py')

# for filename in files:
#   name = __file__
# <body>
# <h1>Service examples for PHP</h1>
#
# <?php
#
#
# $files = glob("../examples/*.php");
# foreach ($files as $filename) {
#     $name = pathinfo($filename)['filename'];
#     $source = highlight_file($filename, true);
#     $output = capture_output(function() use ($filename) {
#         include $filename;
#     });
#
#     print <<<END
# <details>
# <summary>{$name} Sample Code</summary>
# <section>
# <h3>Source</h3>
# {$source}
# </section>
# <section>
# <h3>Output</h3>
# {$output}
# </section>
# </details>
# END;
# }
# ?>
#
# </body>
# </html>
