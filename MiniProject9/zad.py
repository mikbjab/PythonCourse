import abc
import copy
import json
from abc import ABC, abstractmethod
import sys
from typing import Any, Callable


class Item(ABC):
    @property
    @abstractmethod
    def title(self):
        pass

    @property
    @abstractmethod
    def creator(self):
        pass

    @property
    @abstractmethod
    def year(self):
        pass

    @abstractmethod
    def display_info(self):
        pass


class Book(Item):
    def __init__(self, title, author, year, genre, isbn):
        self._title = title
        self._author = author
        self._year = year
        self._genre = genre
        self._isbn = isbn

    @property
    def title(self):
        return self._title

    @property
    def author(self):
        return self._author

    @property
    def year(self):
        return self._year

    @property
    def genre(self):
        return self._genre

    @property
    def isbn(self):
        return self._isbn

    @title.setter
    def title(self, value):
        self._title = value

    @author.setter
    def creator(self, value):
        self._author = value

    @year.setter
    def year(self, value):
        self._year = value

    @genre.setter
    def genre(self, value):
        self._genre = value

    @isbn.setter
    def isbn(self, value):
        self._isbn = value

    def display_info(self):
        print("|".join([self._title, self._author, self._genre, str(self._year), self._isbn]))


class Movie(Item):
    def __init__(self, title, creator, year, genre, dur):
        self._title = title
        self._creator = creator
        self._year = year
        self._genre = genre
        self._duration = dur

    def __eq__(self, other):
        return self.title==other.title and self.creator==other.creator and self.year==other.year

    @property
    def title(self):
        return self._title

    @property
    def creator(self):
        return self._creator

    @property
    def year(self):
        return self._year

    @property
    def genre(self):
        return self._genre

    @property
    def duration(self):
        return self._duration

    @title.setter
    def title(self, value):
        self._title = value

    @creator.setter
    def creator(self, value):
        self._creator = value

    @year.setter
    def year(self, value):
        self._year = value

    @genre.setter
    def genre(self, value):
        self._genre = value

    @duration.setter
    def isbn(self, value):
        self._duration = value

    def display_info(self):
        print("|".join([self._title, self._creator, self._genre, str(self._year), str(self._duration)]))


class Library:
    def __init__(self, list=[]):
        self.items = copy.deepcopy(list)

    def add_item(self, item):
        if isinstance(item, Item):
            self.items.append(item)
        else:
            print("It's not a movie or book")

    def add_items(self,*items):
        for item in items:
            self.add_item(item)

    def display_items(self):
        for item in self.items:
            item.display_info()

    def save_to_file(self, filename):
        with open(filename, "w") as file:
            json.dump(self, file, cls=LibraryJSONEncoder)

    def load_from_file(self, filename):
        with open(filename) as file:
            data = json.load(file)
        for dict_item in data:
            if dict_item["typ"] == "Book":
                self.add_item(Book(dict_item["_title"],
                                   dict_item["_author"],
                                   dict_item["_year"],
                                   dict_item["_genre"],
                                   dict_item["_isbn"]))
            else:
                self.add_item(Movie(dict_item["_title"],
                                    dict_item["_creator"],
                                    dict_item["_year"],
                                    dict_item["_genre"],
                                    dict_item["_duration"]))

    def recommend(self,movie):
        print(f"Movies that are similar to {movie.title}:")
        for item in self.items:
            if isinstance(item,Movie):
                if item==Movie:
                    continue
                if item.genre.lower()==movie.genre.lower():
                    item.display_info()


class LibraryJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Library):
            result = []
            for item in obj.items:
                temp = item.__dict__
                temp["typ"] = item.__class__.__name__
                result.append(temp)
            return result
        return super().default(obj)


lib = Library()
movie1= Movie("Mission Impossible", "Tom Cruise", 2000, "action", 120)
book1=Book("Rhythm of War", "Sanderson", 2022, "fantasy", "ergzscfawg")
lib.add_items(movie1,book1)
book2 = Book("The Great Gatsby", "F. Scott Fitzgerald", 1925, "Classic", "978-3-16-148410-0")
movie2 = Movie("Inception", "Christopher Nolan", 2010, "Sci-Fi", 148)
movie3=Movie("Bourne's Identity","Matt Damon",2002,"Action",119)
lib.display_items()
lib.save_to_file("library.json")

new_library=Library()
new_library.load_from_file("library.json")
new_library.add_items(movie2,book2,movie3)
new_library.display_items()
new_library.recommend(movie3)

