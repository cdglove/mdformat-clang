from pathlib import Path

from markdown_it.utils import read_fixture_file
import mdformat
import pytest

FIXTURE_PATH = Path(__file__).parent / "fixtures.md"
fixtures = read_fixture_file(FIXTURE_PATH)

@pytest.mark.parametrize(
    "line,title,text,expected", fixtures, ids=[f[1] for f in fixtures]
)
def test_fixtures(line, title, text, expected):
    output = mdformat.text(text, codeformatters={
        "cpp",
        "cxx",
        "c++",
        "c",
        "csharp",
        "c#",
        "cs",
        "java",
        "javascript",
        "typescript",
        "ts",
        "json",
        "json-object",
        "objc",
        "obj-c",
        "objectivec",
        "objective-c",
        "protobuf",
        "proto",
        "tablegen",
        "td",
        "verilog",
        "v",
        "objective-c++",
        "objectivec++",
        "obj-c++",
        "objc++"
    })
    print(output)
    assert output.rstrip() == expected.rstrip(), output
