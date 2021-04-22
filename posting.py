#Imports
import nltk
from nltk import word_tokenize
from nltk.corpus import stopwords

stop_words = set(stopwords.words('english'))

class Posting: # This is the main class
    def __init__(self, jsonPosting):
        self.additional_information = "Unspecified"
        self.agency = jsonPosting['agency']
        self.business_title = jsonPosting['business_title']
        self.career_level = "Unspecified"
        self.civil_service_title = jsonPosting['civil_service_title']
        self.division_work_unit = jsonPosting['division_work_unit']
        self.full_time_part_time_indicator = "Unspecified"
        self.hours_shift = "Unspecified"
        self.job_category = "Unspecified"
        self.job_description = jsonPosting['job_description']
        self.job_id = jsonPosting['job_id']
        self.level = jsonPosting['level']
        self.minimum_qual_requirements = "Unspecified"
        self.number_of_positions = jsonPosting['number_of_positions']
        self.post_until = 'Unspecified'
        self.posting_date = jsonPosting['posting_date']
        self.posting_type = jsonPosting['posting_type']
        self.posting_updated = jsonPosting['posting_updated']
        self.preferred_skills = "Unspecified"
        self.process_date = jsonPosting['process_date']
        self.residency_requirement = "Unspecified"
        self.salary_frequency = jsonPosting['salary_frequency']
        self.salary_range_from = jsonPosting['salary_range_from']
        self.salary_range_to = jsonPosting['salary_range_to']
        self.title_classification = jsonPosting['title_classification']
        self.title_code_no = jsonPosting['title_code_no']
        self.to_apply = "Unspecified"
        self.work_location = jsonPosting['work_location']
        self.work_location_1  = "Unspecified"

        #Deal with values that might not exist
        if 'additional_information' in jsonPosting.keys():
          self.additional_information = jsonPosting['additional_information']
        if 'career_level' in jsonPosting.keys():
          self.career_level = jsonPosting['career_level']
        if 'full_time_part_time_indicator' in jsonPosting.keys():
          self.full_time_part_time_indicator = jsonPosting['full_time_part_time_indicator']
        if 'hours_shift' in jsonPosting.keys():
          self.hours_shift = jsonPosting['hours_shift']
        if 'job_category' in jsonPosting.keys():
          self.job_category = jsonPosting['job_category']
        if 'minimum_qual_requirements' in jsonPosting.keys():
          self.minimum_qual_requirements = jsonPosting['minimum_qual_requirements']
        if 'post_until' in jsonPosting.keys():
          self.post_until = jsonPosting['post_until']
        if 'preferred_skills' in jsonPosting.keys():
          self.preferred_skills = jsonPosting['preferred_skills']
        if 'residency_requirement' in jsonPosting.keys():
          self.residency_requirement = jsonPosting['residency_requirement']
        if 'to_apply' in jsonPosting.keys():
          self.to_apply = jsonPosting['to_apply']
        if 'work_location_1' in jsonPosting.keys():
          self.work_location_1 = jsonPosting['work_location_1']

        rawText = self.business_title + " " + self.civil_service_title
        title_Tokens_NLTK = word_tokenize(rawText)
        title_Tokens_NLTK = [w.lower() for w in title_Tokens_NLTK]
        title_Tokens_NLTK = [w for w in title_Tokens_NLTK if not w in stop_words] 
        self.title_NLTK = nltk.Text(title_Tokens_NLTK)

        rawText = self.minimum_qual_requirements + " " + self.preferred_skills
        qualifications_Tokens_NLTK = word_tokenize(rawText)
        qualifications_Tokens_NLTK = [w.lower() for w in qualifications_Tokens_NLTK]
        qualifications_Tokens_NLTK = [w for w in qualifications_Tokens_NLTK if not w in stop_words] 
        self.qualifications_NLTK = nltk.Text(qualifications_Tokens_NLTK)

        rawText = self.salary_range_from + " " + self.salary_range_to
        salary_Tokens_NLTK = word_tokenize(rawText)
        salary_Tokens_NLTK = [w.lower() for w in salary_Tokens_NLTK]
        salary_Tokens_NLTK = [w for w in salary_Tokens_NLTK if not w in stop_words] 
        self.salary_NLTK = nltk.Text(salary_Tokens_NLTK)

        rawText = self.hours_shift
        hours_Tokens_NLTK = word_tokenize(rawText)
        hours_Tokens_NLTK = [w.lower() for w in hours_Tokens_NLTK]
        hours_Tokens_NLTK = [w for w in hours_Tokens_NLTK if not w in stop_words] 
        self.hours_NLTK = nltk.Text(hours_Tokens_NLTK)

        rawText = self.work_location + " " + self.work_location_1
        location_Tokens_NLTK = word_tokenize(rawText)
        location_Tokens_NLTK = [w.lower() for w in location_Tokens_NLTK]
        location_Tokens_NLTK = [w for w in location_Tokens_NLTK if not w in stop_words] 
        self.location_NLTK = nltk.Text(location_Tokens_NLTK)

        rawText = self.job_description
        description_Tokens_NLTK = word_tokenize(rawText)
        description_Tokens_NLTK = [w.lower() for w in description_Tokens_NLTK]
        description_Tokens_NLTK = [w for w in description_Tokens_NLTK if not w in stop_words] 
        self.description_NLTK = nltk.Text(description_Tokens_NLTK)