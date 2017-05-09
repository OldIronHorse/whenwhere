#!/usr/bin/python3

from unittest import main, TestCase

from whenwhere import attendable,Course,distinct_students,Lecture

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
    c=Course('English 101',3,set())
    self.assertEqual([{Lecture(c,1)},{Lecture(c,2)},{Lecture(c,3)}],
                     list(attendable([c])))

  def test_two_courses_no_conflict(self):
    self.maxDiff=None
    c1=Course('English',3,set())
    c2=Course('French',4,set())
    self.assertEqual([{Lecture(c1,1),Lecture(c2,1)},
                      {Lecture(c1,2),Lecture(c2,2)},
                      {Lecture(c1,3),Lecture(c2,3)},
                      {Lecture(c2,4)}],
                     list(attendable([c1,c2])))

  def test_tow_courses_conflict(self):
    self.maxDiff=None
    c1=Course('English',3,{1,2})
    c2=Course('French',4,{2,3})
    self.assertEqual([{Lecture(c1,1)},
                      {Lecture(c1,2)},
                      {Lecture(c1,3)},
                      {Lecture(c2,1)},
                      {Lecture(c2,2)},
                      {Lecture(c2,3)},
                      {Lecture(c2,4)}],
                     list(attendable([c1,c2])))



class TestDistinctStudents(TestCase):
  def test_single_lecture_distinct(self):
    self.assertTrue(distinct_students({Lecture(Course('English',3,{1,2}),10)},
                                      Lecture(Course('French',4,{5,6}),20)))

if __name__=='__main__':
  main()
