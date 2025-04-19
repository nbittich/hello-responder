#!/usr/bin/env python3
# encoding: utf-8

from cortexutils.responder import Responder


class Hello(Responder):
    def __init__(self):
        Responder.__init__(self)
        self.message = self.get_param("config.message", "Hello, world!")

    def run(self):
        Responder.run(self)

        title = self.get_param("data.title", None, "title is missing")
        self.report({"message": f"{self.messgae} - {title}"})

    def operations(self, raw):
        return [self.build_operation("AddTagToCase", tag="we said hello world :)")]


if __name__ == "__main__":
    Hello().run()
