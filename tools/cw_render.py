#!/usr/bin/env python3
"""Offline WeChat-like HTML preview for project markdown; not WeChat publication."""
import argparse
import html
import pathlib
import re

IMAGE = re.compile(r"^【图片(P\d+)｜(.+?)】$")

def render(source):
    out = []
    for line in source.splitlines():
        t = line.strip()
        if not t:
            continue
        if t == "{视频}":
            out.append('<div class="video">{视频}</div>')
        elif (m := IMAGE.fullmatch(t)):
            out.append('<div class="asset">图片 ' + html.escape(m.group(1)) +
                       '｜' + html.escape(m.group(2)) + '</div>')
        elif t.startswith("## "):
            out.append("<h2>" + html.escape(t[3:]) + "</h2>")
        elif t.startswith("# "):
            out.append("<h1>" + html.escape(t[2:]) + "</h1>")
        else:
            out.append("<p>" + html.escape(t) + "</p>")
    css = ('body{font-family:"Microsoft YaHei",sans-serif;background:#fff;'
           'color:#253341;margin:0;padding:20px;line-height:1.85}'
           'article{max-width:720px;margin:auto}h1{font-size:24px}'
           'h2{font-size:19px;color:#008cc4}.asset,.video{padding:35px 15px;'
           'margin:18px 0;background:#f1f6f9;border:1px dashed #abc3d2;'
           'text-align:center;color:#456}')
    return ('<!doctype html><html lang="zh-CN"><meta charset="utf-8">'
            '<meta name="viewport" content="width=device-width, initial-scale=1">'
            '<style>' + css + '</style><article>' + "\n".join(out) +
            '</article></html>')

def main():
    p = argparse.ArgumentParser()
    p.add_argument("input")
    p.add_argument("output")
    args = p.parse_args()
    pathlib.Path(args.output).write_text(
        render(pathlib.Path(args.input).read_text(encoding="utf-8")),
        encoding="utf-8")

if __name__ == "__main__":
    main()
