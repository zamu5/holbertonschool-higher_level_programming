#!/usr/bin/python3
from models.base import Base
from models.rectangle import Rectangle
import unittest
from io import StringIO
from unittest.mock import patch


class TestRectangle(unittest.TestCase):
    def testprubevariables(self):
        rec = Rectangle(3, 4, 5, 6, 7)
        self.assertEqual(rec.width, 3)
        self.assertEqual(rec.height, 4)
        self.assertEqual(rec.x, 5)
        self.assertEqual(rec.y, 6)
        self.assertEqual(rec.id, 7)

    def testsetelements(self):
        rec = Rectangle(1, 2)
        rec.width = 5
        rec.height = 3
        rec.x = 4
        rec.y = 8
        rec.id = 98
        self.assertEqual(rec.width, 5)
        self.assertEqual(rec.height, 3)
        self.assertEqual(rec.x, 4)
        self.assertEqual(rec.y, 8)
        self.assertEqual(rec.id, 98)

    def testcheckattributes(self):
        with self.assertRaises(TypeError):
            r = Rectangle("error", 2)
        with self.assertRaises(TypeError):
            r = Rectangle(2, "error")
        with self.assertRaises(TypeError):
            r = Rectangle((1, 2), 2)
        with self.assertRaises(TypeError):
            r = Rectangle(2, (1, 2))
        with self.assertRaises(TypeError):
            r = Rectangle([1, 2], 2)
        with self.assertRaises(TypeError):
            r = Rectangle(2, [1, 2])
        with self.assertRaises(TypeError):
            r = Rectangle({"a": 1}, 2)
        with self.assertRaises(TypeError):
            r = Rectangle(2, {"a": 1})
        with self.assertRaises(ValueError):
            r = Rectangle(0, 2)
        with self.assertRaises(ValueError):
            r = Rectangle(2, 0)
        with self.assertRaises(ValueError):
            r = Rectangle(-2, 2)
        with self.assertRaises(ValueError):
            r = Rectangle(2, -2)
        with self.assertRaises(TypeError):
            r = Rectangle(0.5, 2)
        with self.assertRaises(TypeError):
            r = Rectangle(2, 0.5)
        with self.assertRaises(TypeError):
            r = Rectangle(2, 2, "error", 2)
        with self.assertRaises(TypeError):
            r = Rectangle(2, 2, 2, "error")
        with self.assertRaises(TypeError):
            r = Rectangle(2, 2, (1, 2), 2)
        with self.assertRaises(TypeError):
            r = Rectangle(2, 2, 2, (1, 2))
        with self.assertRaises(TypeError):
            r = Rectangle(2, 2, [1, 2], 2)
        with self.assertRaises(TypeError):
            r = Rectangle(2, 2, 2, [1, 2])
        with self.assertRaises(TypeError):
            r = Rectangle(2, 2, {"a": 1}, 2)
        with self.assertRaises(TypeError):
            r = Rectangle(2, 2, 2, {"a": 1})
        with self.assertRaises(ValueError):
            r = Rectangle(2, 2, 2, -5)
        with self.assertRaises(ValueError):
            r = Rectangle(2, 2, -2, 5)

    def testarea(self):
        rec = Rectangle(5, 5)
        self.assertEqual(rec.area(), 25)

        rec = Rectangle(5, 5)
        with self.assertRaises(TypeError):
            rec.area(24)

    def testdisplay(self):
        with patch('sys.stdout', new=StringIO()) as salida:
            rec = Rectangle(2, 2)
            rec.display()
            out = "##\n##\n"
            self.assertEqual(salida.getvalue(), out)

        with patch('sys.stdout', new=StringIO()) as salida:
            rec = Rectangle(2, 2, 2, 2)
            rec.display()
            out = "\n\n  ##\n  ##\n"
            self.assertEqual(salida.getvalue(), out)

    def teststri(self):
        rec = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(str(rec), "[Rectangle] (5) 3/4 - 1/2")

    def testupdate(self):
        rec = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(str(rec), "[Rectangle] (5) 3/4 - 1/2")
        rec.update(1, 5, 4, 3, 2)
        self.assertEqual(str(rec), "[Rectangle] (1) 3/2 - 5/4")
