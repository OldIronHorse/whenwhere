#!/usr/bin/env python3

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


def course_groups(courses):
  course_groups=[]
  for c in courses:
    for group in course_groups:
      if distinct_students(group, c):
        group.add(c)
        break
    else:
      course_groups.append({c})
  return course_groups

def distinct_students(courses,course):
  group_students=set()
  for c in courses:
    group_students=group_students.union(c.students)
  return not (group_students & course.students)
