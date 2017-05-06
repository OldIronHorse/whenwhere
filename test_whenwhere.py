#!/usr/bin/python3

from unittest import main, TestCase

from whenwhere import attendable,Course,Lecture

class TestLecture(TestCase):
  def test_equal_true(self):
    self.assertTrue(Lecture('a',1)==Lecture('a',1))

  def test_equal_false_name(self):
    self.assertFalse(Lecture('a',1)==Lecture('b',1))

  def test_equal_false_index(self):
    self.assertFalse(Lecture('a',1)==Lecture('a',2))


class TestAttendable(TestCase):
  def test_empty(self):
    self.assertEqual([],attendable([]))

  def test_single_course(self):
    self.maxDiff=None
    c=Course('English 101',3,[])
    self.assertEqual([{Lecture(c,1)},{Lecture(c,2)},{Lecture(c,3)}],
                     list(attendable([c])))


if __name__=='__main__':
  main()
