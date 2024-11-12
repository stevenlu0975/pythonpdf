from datetime import datetime
from typing import List, Optional
from enum import Enum

# Enums
class DayNight(str, Enum):
    DAY = "日"
    NIGHT = "夜"

class LanguageLevel(str, Enum):
    LEVEL_1 = "1"
    LEVEL_2 = "2"
    LEVEL_3 = "3"
    LEVEL_4 = "4"
    LEVEL_5 = "5"

class IsGraduate(str, Enum):
    GRADUATED = "畢"
    NOT_GRADUATED = "肄"

class SkillLevel(str, Enum):
    VERY_FAMILIAR = "非常熟悉"
    FAMILIAR = "熟悉"
    READ_ONLY = "只讀過"

class YesOrNo(str, Enum):
    YES = "有"
    NO = "沒有"
class RecommendationEnum(str, Enum):
    EMPLOYEE = "員工"
    FRIEND_OR_FAMILY = "親友"

class Gender(str, Enum):
    MALE = "男"
    FEMALE = "女"

class Military(str, Enum):
    COMPLETED = "役畢"
    EXEMPTED = "免役"
    NOT_SERVED = "未役"

class SpecialIdentity(str, Enum):
    DISABILITY = "身心障礙"
    INDIGENOUS = "原住民"
# Classes
class LanguageTable:

    columns_map = {
        "語文": "language",
        "聽": "listen",
        "說": "speak",
        "讀": "read",
        "寫": "write",
        "撰寫\n手冊": "other"
    }
    
    def __init__(
        self,
        language: str,
        listen: LanguageLevel,
        speak: LanguageLevel,
        read: LanguageLevel,
        write: LanguageLevel,
        other: Optional[LanguageLevel] = None,
    ):
        self.language = language
        self.listen = listen
        self.speak = speak
        self.read = read
        self.write = write
        self.other = other

class FamilyTable:
    columns_map = {
        "稱謂": "kinship",
        "姓名": "name",
        "年齡": "age",
        "職業": "career"
    }

    def __init__(self, kinship: str, name: str, age: int, career: str):
        self.kinship = kinship
        self.name = name
        self.age = age
        self.career = career

class Education:
    def __init__(
        self,
        degree: str,
        school_name: str,
        department: str,
        day_night: DayNight,
        start_date: datetime,
        end_date: datetime,
        is_graduate: IsGraduate,
        clubs: Optional[List[str]] = None,
    ):
        self.degree = degree
        self.school_name = school_name
        self.department = department
        self.day_night = day_night
        self.start_date = start_date
        self.end_date = end_date
        self.is_graduate = is_graduate
        self.clubs = clubs if clubs is not None else []

class ComputerSkill:
    def __init__(self, skill: str, skill_level: SkillLevel, tried: YesOrNo):
        self.skill = skill
        self.skill_level = skill_level
        self.tried = tried

class Certification:
    def __init__(self, name: str, organization: str, date: datetime, paper: YesOrNo):
        self.name = name
        self.organization = organization
        self.date = date
        self.paper = paper

class Consultation:
    def __init__(
        self, name: str, company: str, title: str, phone: str, relationship: str
    ):
        self.name = name
        self.company = company
        self.title = title
        self.phone = phone
        self.relationship = relationship

class Experience:
    def __init__(
        self,
        company: str,
        department: str,
        title: str,
        job_description: str,
        is_manager: YesOrNo,
        start_date: datetime,
        end_date: datetime,
        quit_reason: str,
        salary: "Salary",
        annual_salary: "AnnualSalary",
    ):
        self.company = company
        self.department = department
        self.title = title
        self.job_description = job_description
        self.is_manager = is_manager
        self.start_date = start_date
        self.end_date = end_date
        self.quit_reason = quit_reason
        self.salary = salary
        self.annual_salary = annual_salary

class Salary:
    def __init__(
        self,
        fixed_salary: int,
        allowance_name: Optional[str] = None,
        allowance: Optional[int] = 0,
        other_name: Optional[str] = None,
        other: Optional[int] = 0,
        total_salary: Optional[int] = 0,
    ):
        self.fixed_salary = fixed_salary
        self.allowance_name = allowance_name
        self.allowance = allowance
        self.other_name = other_name
        self.other = other
        self.total_salary = total_salary

class AnnualSalary:
    def __init__(
        self, fixed_salary: int, kpi_bonus: int, year_end_bonus: int, total_annual_salary: int
    ):
        self.fixed_salary = fixed_salary
        self.kpi_bonus = kpi_bonus
        self.year_end_bonus = year_end_bonus
        self.total_annual_salary = total_annual_salary

class CreditInfo:
    def __init__(
        self,
        reject: YesOrNo,
        reject_description: str,
        suspend: YesOrNo,
        suspend_description: str,
        illegal: YesOrNo,
        illegal_description: str,
    ):
        self.reject = reject
        self.reject_description = reject_description
        self.suspend = suspend
        self.suspend_description = suspend_description
        self.illegal = illegal
        self.illegal_description = illegal_description

class Relations:
    def __init__(self, name: str, relationship: str, department: str):
        self.name = name
        self.relationship = relationship
        self.department = department


class RecommendationPerson:
    def __init__(self, name: str, person: RecommendationEnum):
        self.name = name
        self.person = person

class Recruition:
    def __init__(self, title: str, fill_date: datetime, is_104: bool, other_website: str, person: RecommendationPerson, 
                 is_hunting: bool, is_return: bool, is_campus: bool, other: str):
        self.title = title
        self.fill_date = fill_date
        self.is_104 = is_104
        self.other_website = other_website
        self.person = person
        self.is_hunting = is_hunting
        self.is_return = is_return
        self.is_campus = is_campus
        self.other = other

class HouseAddress:
    def __init__(self, zipcode: int, address: str, phone: str):
        self.zipcode = zipcode
        self.address = address
        self.phone = phone

class BasicInfo:
    def __init__(self, name: str, eng_name: str, passport_name: str, id_number: str, birth: datetime, gender: Gender, 
                 is_married: bool, military: Military, country: str, height: float, weight: float, habit: str, 
                 special_identity: SpecialIdentity, cellphone: str, email: str, residence_address: HouseAddress, 
                 correspondence_address: HouseAddress, emergency_contactor: str, emergency_relationship: str, 
                 emergency_phone: str):
        self.name = name
        self.eng_name = eng_name
        self.passport_name = passport_name
        self.id_number = id_number
        self.birth = birth
        self.gender = gender
        self.is_married = is_married
        self.military = military
        self.country = country
        self.height = height
        self.weight = weight
        self.habit = habit
        self.special_identity = special_identity
        self.cellphone = cellphone
        self.email = email
        self.residence_address = residence_address
        self.correspondence_address = correspondence_address
        self.emergency_contactor = emergency_contactor
        self.emergency_relationship = emergency_relationship
        self.emergency_phone = emergency_phone

class IBMWorker:
    def __init__(self, is_worked: bool, department: str, title: str, start_date: datetime, end_date: datetime):
        self.is_worked = is_worked
        self.department = department
        self.title = title
        self.start_date = start_date
        self.end_date = end_date

class Expect:
    def __init__(self, salary: int, annual_salary: int, months_of_salary: int, work_date: datetime, wait_days: int):
        self.salary = salary
        self.annual_salary = annual_salary
        self.months_of_salary = months_of_salary
        self.work_date = work_date
        self.wait_days = wait_days

class RelationDetail:
    def __init__(self, people: List[Relations], has_relative: bool, has_boarder: bool, boarder_description: str,
                 has_china: bool, china_description: str, has_contract: bool, contract_description: str, 
                 has_know_how: bool):
        self.people = people
        self.has_relative = has_relative
        self.has_boarder = has_boarder
        self.boarder_description = boarder_description
        self.has_china = has_china
        self.china_description = china_description
        self.has_contract = has_contract
        self.contract_description = contract_description
        self.has_know_how = has_know_how