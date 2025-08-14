# class Tool:
#     count=0
#
#     def __init__(self,name):
#         self.name=name
#         Tool.count += 1
#
#
#
# tool1=Tool('斧头')
# tool2=Tool('斧头')
# tool3=Tool('斧头')
# tool4=Tool('斧头')
# tool5=Tool('斧头')
# # print(Tool.count)
# Tool.count=2
# print(tool1.count)
# print(Tool.count)
# print(tool2.count)


class Tool:
    count=0

    @classmethod
    def show_tool_count(cls):
        print(Tool.count)

    def __init__(self,name):
        self.name=name
        Tool.count += 1

tool1=Tool('斧头')
tool2=Tool('gun')
Tool.show_tool_count()