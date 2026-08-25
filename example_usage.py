from client import AiVettingTechnicalInterviewTalentMatchingClient

def main():
    client = AiVettingTechnicalInterviewTalentMatchingClient()
    res = client.conduct_ai_technical_vetting_and_match('s3://resumes/lead_ai_researcher.pdf', 'Principal AI Alignment Scientist')
    print('Vetting: ' + res['vetting_session_id'] + ' for ' + res['target_role'])
    print('Live AI Interview Score: ' + str(res['live_coding_ai_interview_score_pct']) + '% (' + res['system_design_competency_tier'] + ')')
    print('Salary: ' + res['recommended_salary_range_usd'] + ' | Status: ' + res['talent_placement_match_status'])

if __name__ == '__main__':
    main()
