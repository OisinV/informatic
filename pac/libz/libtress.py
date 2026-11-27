import turtle
import json

class Game:
    def __init__(self):
        self.KeyAction = self.KeyListener()
    
    class CoordinateTranslator:
        """Translates inputted x coordinate to selected node (chunk0 = 0, chunk1 = 1, chunk2 = 2, region0 = 3, region1 = 4), which outputs a usable coordinate tupple."""

        # chunk0 = 0, chunk1 = 1, chunk2 = 2, region0/chunk3 = 3, region1/chunk4 = 4
        def InterpetCoordinatesToHigherNode(self, x:int, y:int):
            hnode = (x // 16, y // 16)
            return hnode # the value of current node level + 1's coords

        def InterpetCoordinatesToLowerNode(self, x:int, y:int):
            lnode = (int(x * 16), int(y * 16))
            return lnode

        def GoHigherNode(self, x:int, y:int, CurrentNode:int, ResultNode:int):
            DeltaNode = ResultNode - CurrentNode

            if DeltaNode < 0:
                raise ValueError("GoHigherNode is intended to have ResultNode larger than CurrentNode.")

            rx = x
            ry = y

            for _ in range(DeltaNode):
                rx, ry = self.InterpetCoordinatesToHigherNode(rx, ry)

            return (rx, ry)

        def GoLowerNode(self, x:int, y:int, CurrentNode:int, ResultNode:int):
            DeltaNode = CurrentNode - ResultNode

            if DeltaNode < 0:
                raise ValueError("GoLowerNode is intended to have CurrentNode larger than LargerNode.")

            rx = x
            ry = y

            for _ in range(DeltaNode):
                rx, ry = self.InterpetCoordinatesToLowerNode(rx, ry)

            return (rx, ry)

        def DetectLorHNode(self, x:int, y:int, CurrentNode:int, ResultNode:int):
            """Instead of knowing up or down, it detects if lower node, or higher node, a safety on it"""
            DeltaNode = ResultNode - CurrentNode

            rx = x
            ry = y

            if DeltaNode < 0:
                for _ in range(abs(DeltaNode)):
                    rx, ry = self.InterpetCoordinatesToLowerNode(rx, ry)
            elif DeltaNode > 0:
                for _ in range(DeltaNode):
                    rx, ry = self.InterpetCoordinatesToHigherNode(rx, ry)
            else:
                print(f"Detect low or high either reached equal or reached unknown (possible issue): Delta = {DeltaNode}, Current = {CurrentNode}, ResultNode = {ResultNode}")

            return (rx, ry)

    class FileInterpetter:
        """Read/Write to file types such as Json or even to sql DBs (if added)."""
        def LoadJsonFile(self, path:str):
            with open(path, "r") as file:
                data = json.load(file)

            return data

        def WriteJsonFile(self, path:str, data:object):
            with open(path, "w") as file:
                json.dump(data, file)

    class KeyListener:
        def __init__(self):
            self.Keys: dict[str, None|object]

        def AddKey(self, Key:str, Fun:object|None):
            self.Keys[Key] = Fun
            pass

    class StartMenu: