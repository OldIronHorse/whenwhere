#!/usr/bin/python3

from itertools import zip_longest

class Lecture:
  def __init__(self,course,index):
    self.course=course
    self.index=index

  def __key(self):
    return (self.course,self.index)

  def __repr__(self):
    return 'Lecture(course={!r},index={!r})'.format(self.course,self.index)

  def __eq__(self,other):
    if isinstance(other,Lecture):
      return self.__key()==other.__key()
    else:
      return NotImplemented

  def __ne__(self,other):
    if not isinstance(other,Lecture):
      return NotImplemented
    else:
      return not self.__eq__(other)

  def __hash__(self):
    return hash(self.__key())


class Course:
  def __init__(self,name,lecture_count,students):
    self.name=name
    self.students=students
    self.lectures=[Lecture(self,n) for n in range(1,lecture_count+1)]

  def __repr__(self):
    return 'Course(name={!r},lecture_count={!r},students={!r})'.format(
      self.name,len(self.lectures),self.students)


def attendable(courses):
  lectures=[]
  for c in courses:
    lectures+=c.lectures
  sequence=[]
  for l in lectures:
    for period in sequence:
      if distinct_students(period, l):
        period.add(l)
    else:
      sequence.append({l})
  return sequence

def distinct_students(period,lecture):
  period_students=set()
  for l in period:
    period_students=period_students.union(l.course.students)
  return not (period_students & lecture.course.students)
  pass
