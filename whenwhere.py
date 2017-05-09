#!/usr/bin/env python3

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
  class_sequences=[]
  return [set(ls) for ls in zip_longest(*[c.lectures for c in courses])]
