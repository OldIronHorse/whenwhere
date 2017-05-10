#!/usr/bin/env python3

from unittest import main,TestCase

from whenwhere import Course,course_groups,distinct_students,Lecture

class TestLecture(TestCase):
  def test_equal_true(self):
    self.assertTrue(Lecture('a',1)==Lecture('a',1))

  def test_equal_false_name(self):
    self.assertFalse(Lecture('a',1)==Lecture('b',1))

  def test_equal_false_index(self):
    self.assertFalse(Lecture('a',1)==Lecture('a',2))


class TestCourseGroups(TestCase):
  def test_empty(self):
    self.assertEqual([],course_groups([]))

  def test_single_course(self):
    self.maxDiff=None
    c=Course('English 101',3,set())
    self.assertEqual([{c}],list(course_groups([c])))

  def test_two_courses_no_conflict(self):
    self.maxDiff=None
    c1=Course('English',3,set())
    c2=Course('French',4,set())
    self.assertEqual([{c1,c2}],course_groups([c1,c2]))

  def test_tow_courses_conflict(self):
    self.maxDiff=None
    c1=Course('English',3,{1,2})
    c2=Course('French',4,{2,3})
    self.assertEqual([{(c1)},{c2}],course_groups([c1,c2]))

#TODO test for multiple courses, some conflicting



class TestDistinctStudents(TestCase):
  def test_single_lecture_distinct(self):
    self.assertTrue(distinct_students([Course('English',3,{1,2})],
                                      Course('French',4,{5,6})))

  def test_single_lecture_not_distinct(self):
    self.assertFalse(distinct_students([Course('English',3,{1,2})],
                                       Course('French',4,{2,6})))

  def test_lectures_distinct(self):
    self.assertTrue(distinct_students([Course('English',3,{1,2}),
                                       Course('Maths',3,{3,4})],
                                      Course('French',4,{5,6})))

  def test_lectures_not_distinct(self):
    self.assertFalse(distinct_students([Course('English',3,{1,2}),
                                        Course('Maths',3,{3,4})],
                                       Course('French',4,{3,6})))


if __name__=='__main__':
  main()
