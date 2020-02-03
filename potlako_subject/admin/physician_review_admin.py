from django.contrib import admin
from import_export.admin import ImportExportActionModelAdmin
from ..admin_site import potlako_subject_admin
from ..forms import PhysicianReviewForm
from ..models import PhysicianReview


@admin.register(PhysicianReview, site=potlako_subject_admin)
class PhysicianReviewAdmin(ImportExportActionModelAdmin, admin.ModelAdmin):

    form = PhysicianReviewForm

    fieldsets = (
        (None, {
            'fields': ('review_date_time',
                       'reviewer_name',
                       'reviewer_other',
                       'physician_summary',
                       'diagnosis_plan',
                       'needs_discussion',
                       'coordinator_summary',
                       'cancer_eval',
                       'reason_fu_needed',
                       'final_status',
                       'non_cancer_diagnosis',
                       'non_cancer_diagnosis_other',
                       'cancer_diagnosis',
                       'cancer_diagnosis_other',
                       'to_be_flagged'),
        }),
    )

    radio_fields = {'reviewer_name': admin.VERTICAL,
                    'needs_discussion': admin.VERTICAL,
                    'cancer_eval': admin.VERTICAL,
                    'final_status': admin.VERTICAL,
                    'non_cancer_diagnosis': admin.VERTICAL,
                    'cancer_diagnosis': admin.VERTICAL,
                    'to_be_flagged': admin.VERTICAL,
                    }
