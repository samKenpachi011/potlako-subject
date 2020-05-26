from edc_constants.constants import (
    ALIVE, DEAD, OTHER, OFF_STUDY, UNKNOWN, NOT_APPLICABLE, NONE)

from .constants import UNSURE

ALIVE_DEAD_LTFU = (
    (ALIVE, 'Patient alive (specify)'),
    (DEAD, 'Patient died'),
    ('ltfu', 'Patient lost to follow up'),
    (OTHER, 'Other (specify)'),
)

APPT_CHANGE_REASON = (
    ('providers_changed_appt', 'Providers changed appointment date'),
    ('missed_appointment', 'I missed the appointment'),
    ('changed_appointment', 'I contacted clinic to change the appointment date'),
    (OTHER, 'Other (specify)'),
)

BUS_VOUCHER_STATUS = (
    ('not_drafted', 'Letter not yet drafted'),
    ('not_sent', 'Letter completed but not yet sent to facility'),
    ('not_received', 'Letter sent to facility (but not yet received)'),
    ('patient_received', 'Letter received by patient'),
    (OTHER, 'Other (specify)'),
    (NOT_APPLICABLE, 'N/A'),
)

CANCER_DIAGNOSIS = (
    ('cervical', 'Cervical Cancer'),
    ('breast', 'Breast Cancer'),
    ('head_n_neck', 'Head and Neck Cancer'),
    ('non_hodgkin_lymph', 'Non-Hodgkin Lymphoma'),
    ('hodgkin_lymph', 'Hodgkin Lymphoma'),
    ('esophageal', 'Esophageal'),
    ('vuginal', 'Vulvar/Vaginal Cancer'),
    ('anal', 'Anal Cancer'),
    ('kaposis_sarcoma', 'Kaposi\'s sarcoma'),
    ('penile', 'Penile Cancer'),
    ('prostate', 'Prostate Cancer'),
    ('colorectal', 'Colorectal Cancer'),
    (OTHER, 'Other'),
)

CANCER_EVALUATION = (
    ('complete', 'Complete'),
    ('unable_to_complete',
     'Incomplete, but unable to complete (i.e. death, refusal)'),
    ('incomplete_needs_priority',
     'Incomplete, needs priority Potlako+ follow-up'),
    ('complete_needs_priority', 'Complete, needs priority Potlako+ follow-up')
)

CANCER_STAGES = (
    ('stage_0', 'Stage 0'),
    ('stage_I', 'Stage I'),
    ('stage_II', 'Stage II'),
    ('stage_III', 'Stage III'),
    ('stage_IV', 'Stage IV'),
)

CANCER_STATUS = (
    ('confirmed', 'Confirmed cancer'),
    ('probable', 'Probable cancer'),
    ('possible_not', 'Possible not cancer'),
    ('probable_not', 'Probable not cancer, no alternative dx'),
    ('confirmed_not', 'Confirmed not cancer, alternative dx'),
    ('incomplete_dx', 'Incomplete dx'),
)

CASH_TRANSFER_STATUS = (
    ('not_initiated', 'Transaction not yet initiated'),
    ('successful_confirmed', 'Transaction successful and patient confirmed'),
    ('successful_unconfirmed', 'Transaction successful but no patient '
     'confirmation'),
    ('not_successful', 'Transaction not successful (specify)'),
    (NOT_APPLICABLE, 'N/A'),
)

CANCER_SUSPECT = (
    ('call_with_clinician', 'Phone call with clinician'),
    ('review_clinic_register', 'Review of clinic register'),
    ('clinician_site_visit_discussion', 'Site visit discussion with clinician'),
    (OTHER, 'Other (specify)')
)

CLINICIAN_TYPE = (
    ('med_officer', 'Medical Officer'),
    ('nurse', 'Nurse'),
    ('smo/cmo', 'SMO/CMO'),
    ('research_team', 'Research team'),
    (OTHER, 'Other type (specify)')
)

COMPONENTS_RECEIVED = (
    ('provider_edication', 'Provider education'),
    ('diagnostic_facilitation', 'Diagnostic facilitation (pre-biopsy/test)'),
    ('access_to_diagnostic_results',
     'Access to diagnostic results (e.g. histology)'),
    ('cancer_treatment_facilitation_post_test_results',
     'Cancer treatment facilitation post-test results'),
    ('retention_or_completion_of_cancer_treatment',
     'Retention or completion of cancer treatment'),
    (NONE, 'None'),
    (OTHER, 'Other (specify)'),
)

DEATH_INFO_SOURCE = (
    ('clinician', 'Clinician'),
    ('next_of_kin1', 'Next of kin 1'),
    ('next_of_kin2', 'Next of kin 2'),
    ('other_fam_member', 'Other family member'),
    (OTHER, 'Other (specify)'),
)

DETERMINE_MISSED_VISIT = (
    ('database',
     'Research staff referenced database and contacted clinician/facility'),
    ('clinic_register',
     'Clinician referenced clinic register and contacted research staff'),
    ('clinician_contacted', 'Patient contacted clinician'),
    ('research_staff_contacted', 'Patient contacted research staff'),
    (OTHER, 'Other (specify)')
)

DELAYED_REASON = (
    ('patient_factor', 'Patient Factor'),
    ('health_system_factor', 'Health System Factor')
)

DIAGNOSIS_RESULTS = (
    ('malignant', 'Malignant'),
    ('non_malignant', 'Non Malignant'),
)

DISPOSITION = (
    ('return', 'Return'),
    ('refer', 'Refer'),
    ('discharge', 'Discharge')
)

DISTRICT = (
    ('bokaa', 'Bokaa'),
    ('lentsweletau', 'Lentsweletau'),
    ('lerala', 'Lerala'),
    ('letlhakeng', 'Letlhakeng'),
    ('mandunyane', 'Mandunyane'),
    ('mathangwane', 'Mathangwane'),
    ('maunatlala', 'Maunatlala'),
    ('masunga', 'Masunga'),
    ('metsimotlhabe', 'Metsimotlhabe'),
    ('mmadinare', 'Mmadinare'),
    ('mmandunyane', 'Mmandunyane'),
    ('mmankgodi', 'Mmankgodi'),
    ('mmathethe', 'Mmathethe'),
    ('molapowabojang', 'Molapowabojang'),
    ('nata', 'Nata'),
    ('oodi', 'Oodi'),
    ('otse', 'Otse'),
    ('ramokgonami', 'Ramokgonami'),
    ('sefhophe', 'Sefhophe'),
    ('tati_siding', 'Tati Siding'),
)

DURATION = (
    ('days', 'Days'),
    ('weeks', 'Weeks'),
    ('months', 'Months'),
    ('years', 'Years')
)

DATE_ESTIMATION = (
    ('day', 'Estimated day only'),
    ('day_month', 'Estimated day and month'),
    ('month', 'Estimated month only'),
    ('year', 'Estimate year only'),
    ('day_month_year', 'Estimated day, month and year')
)

DATE_TIME_ESTIMATION = (
    ('time', 'Estimated time only'),
    ('time_day', 'Estimated time and day'),
    ('day', 'Estimated day only'),
    ('day_month', 'Estimated day and month'),
    ('month', 'Estimated month only'),
    ('year', 'Estimate year only'),
    ('day_month_year', 'Estimated day, month and year')
)

EDUCATION_LEVEL = (
    ('non_formal', 'Non-Formal'),
    ('primary', 'Primary'),
    ('secondary', 'Secondary'),
    ('tertiary', 'Tertiary'))

ENROLLMENT_SITES = (
    ('mmathethe_clinic', 'Mmathethe clinic'),
    ('molapowabojang_clinic', 'Molapowabojang clinic'),
    ('otse_clinic', 'Otse clinic'),
    ('mmankgodi_clinic', 'Mmankgodi clinic'),
    ('leentsweletau_clinic', 'Lentsweletau clinic'),
    ('letlhakeng_clinic', 'Letlhakeng clinic'),
    ('oodi_clinic', 'Oodi clinic'),
    ('bokaa_clinic', 'Bokaa clinic'),
    ('metsimotlhabe_clinic', 'Metsimotlhabe clinic'),
    ('shoshong_clinic', 'Shoshong clinic'),
    ('sheleketla_clinic', 'Sheleketla clinic'),
    ('ramokgonami_clinic', 'Ramokgonami clinic'),
    ('lerala_clinic', 'Lerala clinic'),
    ('maunatlala_clinic', 'Maunatlala clinic'),
    ('sefophe_clinic', 'Sefophe clinic'),
    ('mmadianare_primary_hospital', 'Mmadinare Primary Hospital'),
    ('manga_clinic', 'Manga clinic'),
    ('mandunyane_clinic', 'Mandunyane clinic'),
    ('mathangwane_clinic', 'Mathangwane clinic'),
    ('tati_siding_clinic', 'Tati Siding clinic'),
    ('masunga_primary_hospital', 'Masunga Primary Hospital'),
    ('masunga_clinic', 'Masunga clinic'),
    ('nata_clinic', 'Nata clinic')

)

ENROLLMENT_VISIT_METHOD = (
    ('walked', 'Walked'),
    ('patient_drove_themselves', 'Patient Drove Themselves'),
    ('patient_driven_by_someone', 'Patient Was Driven By Someone'),
    ('special_taxi', 'Special Taxi'),
    (OTHER, 'Other (specify)')
)

FACILITY = (
    ('athlone_hospital', 'Athlone Hospital'),
    ('bamalete_lutheran_hospital', 'Bamalete Lutheran Hospital'),
    ('bokaa_clinic', 'Bokaa clinic'),
    ('deborah_reteif_memorial_hospital', 'Deborah. Reteif. Memorial Hospital'),
    ('goodhope_hospital', 'Goodhope Hospital'),
    ('gweta_hospital', 'Gweta Hospital'),
    ('kanye_sda_hospital', 'Kanye SDA Hospital'),
    ('lentsweletau_clinic', 'Lentsweletau clinic'),
    ('lerala_clinic', 'Lerala clinic'),
    ('letlhakeng_clinic', 'Letlhakeng clinic'),
    ('mahalapye_hospital', 'Mahalapye Hospital'),
    ('mandunyane_clinic', 'Mandunyane clinic'),
    ('manga_clinic', 'Manga clinic'),
    ('masunga_primary_hospital', 'Masunga Primary Hospital'),
    ('masunga_clinic', 'Masunga clinic'),
    ('mathangwane_clinic', 'Mathangwane clinic'),
    ('maunatlala_clinic', 'Maunatlala clinic'),
    ('metsimotlhabe_clinic', 'Metsimotlhabe clinic'),
    ('mmadianare_primary_hospital', 'Mmadinare Primary Hospital'),
    ('mmankgodi_clinic', 'Mmankgodi clinic'),
    ('mmathethe_clinic', 'Mmathethe clinic'),
    ('molapowabojang_clinic', 'Molapowabojang clinic'),
    ('nata_clinic', 'Nata clinic'),
    ('nyangagwe_hospital', 'Nyangagwe Hospital'),
    ('oodi_clinic', 'Oodi clinic'),
    ('otse_clinic', 'Otse clinic'),
    ('palapye_hospital', 'Palapye Hospital'),
    ('princess_marina_hospital', 'Princess Marina Hospital'),
    ('ramokgonami_clinic', 'Ramokgonami clinic'),
    ('scottish_livingstone_hospital', 'Scottish Livingstone Hospital'),
    ('sefophe_clinic', 'Sefophe clinic'),
    ('selibe_phikwe_hospital', 'Selibe Phikwe Hospital'),
    ('sheleketla_clinic', 'Sheleketla clinic'),
    ('shoshong_clinic', 'Shoshong clinic'),
    ('tati_siding_clinic', 'Tati Siding clinic'),
    ('thamaga_hospital', 'Thamaga Hospital'),
    (OTHER, 'Other (specify)')

)

FACILITY_TYPE = (
    ('health_post', 'health post'),
    ('primary_clinic', 'primary clinic'),
    ('primary_hospital', 'primary hospital'),
    ('secondary_hospital', 'secondary hospital'),
    ('referral_hospital', 'referral hospital')
)

FACILITY_UNIT = (
    ('OPD', 'OPD'),
    ('A&E', 'A&E'),
    ('IDCC', 'IDCC'),
    ('medicine_clinic', 'Medicine clinic'),
    ('GYN_clnic', 'GYN clinic'),
    ('surgery_clinic', 'Surgery clinic'),
    (NOT_APPLICABLE, 'Not applicable'),
    (OTHER, 'Other'),
)

HEALTH_FACTOR = (
    ('clinic_hospital_unable_schedule_2_weeks', 'Clinic/hospital unable to '
     'schedule within 2 weeks (overbooked, uncertain schedule, etc)'),
    ('clinic_hospital_did_not_schedule_2_weeks', 'Clinic/hospital did not '
     'schedule within 2 weeks (unwilling, low priority case, etc)'),
    ('clinic_no_transport', 'Clinic/hospital provided transportation not '
     'available (needed for other clinic use, broken, driver on leave, etc)'),
    ('service_unavailable',
     'Clinic/hospital service no available on scheduled date (surgical '
     'consultation, biopsy clinic, etc)'),
    ('service_provider_not_available',
     'Clinic/hospital provider not  available on scheduled date (provider '
     'called to emergency, provider on leave, etc)'),
    ('supplies_not_available', 'Clinic/hospital supplies not available on '
     'scheduled date (no biopsy needles, out of stock chemotherapy, etc)'),
    (OTHER, 'other clinic or hospital related reason (specify)')
)

IDENTITY_TYPE = (
    ('country_id', 'Country ID number'),
    ('passport', 'Passport'),
    ('birth_certificate', 'Birth Certificate'),
    (OTHER, 'Other'),
)

IMAGING_STATUS = (
    ('ordered', 'Ordered'),
    ('performed', 'Performed')
)

IMAGING_TESTS = (
    ('xray_chest', 'Xray - chest'),
    ('xray_other', 'Xray - other (specify)'),
    ('ultrasound_abdomen', 'Ultrasound - abdomen'),
    ('ultrasound_other', 'Ultrasound - other (specify)'),
    ('CT', 'CT (specify)'),
    ('MRI', 'MRI (specify)'),
    (OTHER, 'Other imaging test (specify)')
)

KIN_RELATIONSHIP = (
    ('spouse', 'Spouse'),
    ('child', 'Child'),
    ('parent', 'Parent'),
    ('sibling', 'Sibling'),
    ('grandparents', 'Grandparents'),
    ('grandchild', 'Grandchild'),
    (OTHER, 'Other')
)

LAB_TESTS = (
    ('FBC', 'FBC'),
    ('RFT', 'RFT'),
    ('LFT', 'LFT'),
    ('HIV', 'HIV'),
    ('WBC', 'WBC'),
    ('Hb', 'Hb'),
    ('Plt', 'Plt'),
    ('Cr', 'Cr'),
    ('K', 'K'),
    ('Na', 'Na'),
    ('Glu', 'Glu'),
    ('pap_smear', 'Pap Smear'),
    (OTHER, 'Other lab test (specify)')
)

LAB_TESTS_STATUS = (
    ('ordered', 'Ordered'),
    ('specimen_taken', 'Specimen taken'),
    ('specimen_logged_ipms', 'Specimen logged into IPMS'),
    ('specimen_recieved_nhl', 'Specimen received at NHL (for pathology only)'),
    ('results_available_ipms', 'Results available on IPMS'),
    ('results_available_paper', 'Results available on paper'),
    (OTHER, 'Other (specify)')
)

LTFU_CRITERIA = (
    ('missed_visits', 'Missed visits'),
    ('attempted_calls_to_patient',
     'attempted calls to patient x 3 or 3 different days'),
    ('attempted_calls_to_next_kin1',
     'attempted calls to next of kin 1 x 3 or 3 different days'),
    ('attempted_calls_to_next_kin2',
     'attempted calls to next of kin 2 x 3 or 3 different days'),
    ('home_visit_done_unable_to_trace', 'home visit done and unable to trace'),
)

MEDICAL_CONDITION = (
    ('cardiac_condition', 'Cardiac Condition'),
    ('metabolic_disease', 'Metabolic Disease'),
    ('respiratory_disease', 'Respiratory Disease'),
    ('neurological_disease', 'Neurological Disease'),
    ('musculoskeletal_disease', 'Muscoloskeletal Disease'),
    ('skin_disease', 'Skin Disease'),
    ('psychiatric_condition', 'Psychiatric Condition'),
    ('genitourinary_disease', 'Genitourinary Disease'),
    ('gastroenterological_disease', 'Gastroenterological Disease'),
    (OTHER, 'Other (Specify')
)

NON_CANCER_DIAGNOSIS = (
    ('fibroadenoma', 'Fibroadenoma'),
    ('breast_cyst', 'Breast cyst'),
    ('breast_abscess', 'Breast Abscess'),
    ('tb', 'Tuberculosis'),
    ('skin_ulcer', 'Non-healing skin ulcer'),
    ('pre_cancerous_lesion', 'Cervical pre-cancerous lesion'),
    ('no_alt_diagnosis_est', 'No alternative diagnosis established'),
    (OTHER, 'Other'),
)

NOTES = (
    ('LFTs', 'LFTs'),
    ('U&Es', 'U&Es'),
    ('ESR', 'ESR'),
    ('FBC', 'FBC'),
    ('CXR', 'CXR'),
    ('USS', 'USS'),
    ('U/A', 'U/A'),
    ('microscopy', 'Microscopy'),
    (NOT_APPLICABLE, 'Not applicable'),
    (OTHER, 'Other (specify)'),
)

PATIENT_FACTOR = (
    ('patient_work_obligations', 'Patient work obligations (formal '
     'and informal work, including lands and cattle post)'),
    ('patient_family_obligations', 'Patient family obligations '
     '(childcare, funeral, illness in family, etc)'),
    ('patient_paying_transport_difficulty', 'Patient difficulty paying for '
     'transportation, including family member to accompany'),
    ('patient_finding_tarnsport_difficulty', 'Patient difficulty finding '
     'transportation or family member to accompany'),
    (OTHER, 'Other patient related reason (specify)')
)

PEOPLE_INQUIRED_FROM = (
    ('patient_called', 'Patient called (phone answered)'),
    ('kin1_called',
     'Next of kin 1 called (phone answered) after patient called (NO answer, '
     'SMS sent)'),
    ('kin2_called', 'Next of kin 2 called (phone answered) after patient and '
     'next of kin 1 called (NO answer for both, SMS sent to both)'),
    ('unreachable', 'Unable to reach patient or next of kin'),
)

PLACE_OF_DEATH = (
    ('home', 'At home or in the community'),
    ('facility', 'At facility'),
    (UNKNOWN, 'Place of death unknown'),
)

PATHOLOGY_TEST_TYPE = (
    ('biopsy_bone_marrow', 'Biopsy - bone marrow'),
    ('biopsy_lymph_node', 'Biopsy - lymph node'),
    ('biopsy_other', 'Biopsy - other (specify)'),
    ('FNA', 'FNA'),
    ('pap_smear', 'Pap smear')
)

PAIN_SCORE = (
    (1, '1'),
    (2, '2'),
    (3, '3'),
    (4, '4'),
    (5, '5')
)

REASON_FOR_EXIT = (
    ('death', 'Patient death'),
    ('ltfu', 'Patient lost to follow-up'),
    ('eval_complete', 'Cancer evaluation complete'),
    ('declines_further_eval',
     'Patient or clinician declines further evaluation'),
    ('patient_requests_removal', 'Patient requests removal from Potlako+'),
    ('clinician_requests_removal', 'Clinician requests removal from Potlako+'),
)

REASON_MISSED_VISIT = (
    ('no_appointment_knowledge', 'Did not know about appointment'),
    ('forgot_appointment', 'Did not remember appointment date'),
    ('no_transport_fare', 'Could not afford transport fee'),
    ('no_access_to_transport', 'Did not have access to transportation'),
    ('different_facility', 'Went to a different facility'),
    ('felt_better',
     'Did not think they had to come in because feeling better'),
    ('didnt_think_theyd_get_help',
     'Did not wish to return because they did not think they would get help'),
    ('deceased', 'Patient deceased'),
    (OTHER, 'Other (specify)'),
)

REVIEWER = (
    ('Neo', 'Neo'),
    ('Scott', 'Scott'),
    (OTHER, 'Other')
)

SCALE = (
    (0,
     '0 - Fully active, able to carry on all pre-disease performance '
     'without restriction'),
    (1,
     '1 - Restricted in physically strenuous activity but ambulatory and '
     'able to carry out work of a light or sedentary nature, e.g., light '
     'house work, office work'),
    (2,
     '2 - Ambulatory and capable of all selfcare but unable to carry out any '
     'work activities; up and about more than 50% of waking hours'),
    (3,
     '3 - Capable of only limited selfcare; confined to bed or chair more '
     'than 50% of waking hours'),
    (4,
     '4 - Completely disabled; cannot carry on any selfcare; totally '
     'confined to bed or chair'),
    (5,
     '5 - Dead')
)

SEVERITY_LEVEL = (
    ('low', 'Low'),
    ('moderate', 'Moderate'),
    ('high', 'High')
)

SMS_OUTCOME = (
    ('patient_sent_sms_received', 'SMS sent to patient and receipt confirmed'),
    ('patient_sent_sms_not_received', 'SMS sent to patient and receipt NOT '
     'confirmed'),
    ('kin1_sent_sms_received', 'SMS sent to next of kin 1 and receipt '
     'confirmed'),
    ('kin1_sent_sms_not_received',
     'SMS sent to next of kin 1 and receipt NOT confirmed'),
    ('kin2_sent_sms_received', 'SMS sent to next of kin 2 and receipt '
     'confirmed'),
    ('kin2_sent_sms_not_received',
     'SMS sent to next of kin 2 and receipt NOT confirmed'),
)

SUSPECTED_CANCER = (
    ('breast', 'Breast'),
    ('vulva', 'Vulva'),
    ('penile', 'Penile'),
    ('cervical', 'Cervical'),
    ('head_neck', 'Head and Neck'),
    ('vaginal', 'Vaginal'),
    ('prostate', 'Prostate'),
    ('kaposi_sarcoma', 'Kaposi Sarcoma'),
    (UNSURE, 'Unsure'),
    (OTHER, 'Other (specify)'),
)

TRANSPORT_TYPE = (
    ('facility_vehicle', 'Facility Vehicle - Arranged by RC'),
    ('bus', 'Bus Voucher'),
    ('cash', 'Cash transfer to patient'),
    ('patient_arranged_vehicle',
     'Facility Vehicle - Arranged by Patient or Clinician'),
)

TREATMENT_TYPE = (
    ('oral', 'Oral medications'),
    ('suppositories', 'Suppositories'),
    ('injectable', 'Injectable'),
    ('topical_ointment', 'Topical/Ointment'),
    ('inhalation', 'Inhalation'),
    ('drops', 'Drops')
)

TREATMENT_INTENT = (
    ('curative', 'Curative'),
    ('palliative', 'Palliative'),
    ('uncertain', 'Uncertain'),
)

TRIAGE_STATUS = (
    ('emergency', 'Emergency'),
    ('urgent', 'Urgent'),
    ('routine', 'Routine'),
)

UNEMPLOYED_REASON = (
    ('pensioner', 'Pensioner'),
    ('senior_citizen', 'Senior Citizen'),
    ('does_not_want', 'Does not want to work'),
    ('looking', 'Looking for a job'),
    ('too_sick', 'Too sick to work'),
    ('disabled', 'Disabled'),
    (OTHER, 'Other (specify)'),
)

VEHICLE_ARR_STATUS = (
    ('in_progress', 'Request made to facility, arrangement in progress'),
    ('to_be_communicated',
     'Arrangement confirmed by facility but not yet communicated with '
     'patient or clinician'),
    ('confirmed_communicated',
     'Arrangement confirmed by facility and communicated to the patient '
     'and clinician'),
    ('vehicle_cannot_be_provided', 'Request made facility NOT able to '
     'provide transport/vehicle for patient'),
    (OTHER, 'Other (specify)'),
    (NOT_APPLICABLE, 'N/A'),
)

VISIT_TYPE = (
    ('referral', 'Referral'),
    ('return', 'Return'),
)

VISIT_UNSCHEDULED_REASON_CHOICE = (
    ('routine_oncology_clinic_visit',
     'Routine oncology clinic visit (i.e. planned chemo, follow-up)'),
    ('ill_oncology_clinic_visit', 'Ill oncology clinic visit'),
    ('patient_called_to_come_for_visit', 'Patient called to come for visit'),
    (OTHER, 'Other, specify: '),
)

VISIT_UNSCHEDULED_REASON = (
    ('routine_oncology', 'Routine oncology clinic visit (i.e. planned chemo, follow-up)'),
    ('ill_oncology', 'Ill oncology clinic visit'),
    ('patient_called', 'Patient called to come for visit'),
    (NOT_APPLICABLE, 'Not Applicable'),
    (OTHER, 'Other, specify:'),
)

VISIT_REASON = (
    ('initial_visit/contact', 'Initial visit/contact'),
    ('quarterly_visit/contact', 'Quarterly visit/contact'),
    ('unscheduled_visit/contact', 'Unscheduled visit/contact'),
    ('missed_quarterly_visit', 'Missed quarterly visit'),
    ('lost_to_follow_up', 'Lost to follow-up (use only when taking subject off study)'),
    ('death', 'Death'),
    (OFF_STUDY, 'Off study'),
    ('deferred', 'Deferred'),
)

VISIT_INFO_SOURCE = (
    ('clinic_visit', 'Clinic visit with participant'),
    ('other_contact_subject', 'Other contact with participant (i.e telephone call)'),
    ('contact_health worker', 'Contact with health care worker'),
    ('contact_family/designated_person',
     'Contact with family or designated person who can provide information'),
    (OTHER, 'Other,specify'),
)

WORK_TYPE = (
    ('formal_employment', 'Formal employment'),
    ('temporary_employment', 'Temporary Employment'),
    ('part_time_employment', 'Part-Time Employment'),
    ('self_employed', 'Self Employed'),
    ('retired', 'Retired'),
    (OTHER, 'Other,specify')
)
