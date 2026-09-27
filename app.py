"""
BB College Student Portal Management System (BBCSPMS)
Python AI Copilot, Document Analysis, and Machine Learning Microservice
"""
import os
import sys
from flask import Flask, request, jsonify
from flask_cors import CORS

from ml_models.risk_model import StudentAcademicRiskPredictor
from file_analysis.doc_analyzer import DocumentAnalyzer

app = Flask(__name__)
CORS(app)

risk_predictor = StudentAcademicRiskPredictor()
doc_analyzer = DocumentAnalyzer()

@app.route('/health', methods=['GET'])
def health():
    return jsonify({
        'status': 'healthy',
        'service': 'BBCSPMS AI & Machine Learning Microservice',
        'college': 'BB College (Affiliated to KNU)',
        'version': '2.0.0'
    })

@app.route('/api/ml/predict-student-risk', methods=['POST'])
def predict_student_risk():
    """
    Predicts academic drop-out/backlog risk for a student.
    Matches EduNova AI ERP Risk Alert System.
    """
    try:
        data = request.get_json() or {}
        result = risk_predictor.predict_risk(data)
        return jsonify({
            'success': True,
            'data': result
        })
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 400

@app.route('/api/ml/analyze-document', methods=['POST'])
def analyze_document():
    """
    Validates uploaded document files, analyzes format integrity and size.
    """
    try:
        data = request.get_json() or {}
        file_path = data.get('file_path')
        doc_type = data.get('doc_type', 'General')
        
        if not file_path:
            return jsonify({'success': False, 'error': 'file_path is required'}), 400
            
        result = doc_analyzer.analyze_document(file_path, doc_type)
        return jsonify(result)
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 400

@app.route('/api/ml/ai-copilot', methods=['POST'])
def ai_copilot():
    """
    Autonomous Academic Copilot for BB College & KNU queries.
    Provides verified institutional responses, syllabus advice, exam rules, and attendance criteria.
    """
    try:
        data = request.get_json() or {}
        query = (data.get('query') or '').strip().lower()
        role = data.get('role', 'student')
        student_id = data.get('student_id')

        # Academic Knowledge Base & Policy Grounding
        response_text = ""
        context_data = {}

        if 'attendance' in query:
            response_text = (
                "Under Kazi Nazrul University (KNU) Academic Regulations, a minimum of 75% attendance "
                "in lectures and practical tutorials is mandatory to be eligible for regular semester examinations. "
                "Students with 60% to 74% attendance may seek condonation on verified medical grounds approved by the Principal. "
                "Attendance below 60% results in exam debarment."
            )
            context_data = {'min_attendance': 75, 'condonation_range': '60-74%'}

        elif 'backlog' in query:
            response_text = (
                "BB College policy strictly restricts Guardian portal access if a student has an active uncleared backlog. "
                "Students with semester backlogs can register for supplementary backlog examinations in the corresponding "
                "odd or even semester exam cycle through the KNU examination portal after paying the backlog fee of ₹350 per paper."
            )
            context_data = {'backlog_fee_per_paper': 350, 'guardian_access_rule': 'Blocked on active backlog'}

        elif 'combined marksheet' in query or 'final result' in query:
            response_text = (
                "The 8-Semester Combined Marksheet is generated upon successful completion and clearing of all 8 semesters "
                "(Semesters 1 through 8). It aggregates credits, SGPA across all semesters, and calculates the final cumulative CGPA "
                "and division according to KNU 10-point grading guidelines."
            )
            context_data = {'semesters': 8, 'grading_scale': '10-point UGC/KNU'}

        elif 'library' in query or 'library card' in query:
            response_text = (
                "BB College Premium Library Cards are issued for a duration of 4 Years. Students can borrow up to 3 books "
                "simultaneously for 14 days. Late returns incur a nominal fine of ₹2 per day. Digital cards feature high-resolution "
                "QR codes for automated checkout."
            )
            context_data = {'card_validity_years': 4, 'max_books': 3, 'loan_period_days': 14}

        elif 'admit card' in query:
            response_text = (
                "Admit cards are generated digitally once exam registration is verified, course fees are cleared, "
                "and the student maintains at least 75% attendance. Each admit card contains a secure QR verification code "
                "verifiable at the exam centre."
            )
            context_data = {'qr_verification': True}

        else:
            response_text = (
                f"BB College Academic Copilot: Received inquiry '{query}'. "
                "BBCSPMS is fully integrated with Kazi Nazrul University regulations. "
                "You can ask me regarding attendance criteria, exam registration, syllabus breakdown, "
                "backlog rules, 4-year library cards, or fee payment schedules."
            )

        return jsonify({
            'success': True,
            'response': response_text,
            'context': context_data
        })
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 400

@app.route('/api/ml/generate-lesson-plan', methods=['POST'])
def generate_lesson_plan():
    """
    AI Lesson Planner matching EduNova AI ERP screenshot.
    """
    try:
        data = request.get_json() or {}
        subject = data.get('subject', 'Computer Science')
        topic = data.get('topic', 'Data Structures & Algorithms')
        duration_mins = data.get('duration_mins', 60)

        plan = {
            'subject': subject,
            'topic': topic,
            'duration_mins': duration_mins,
            'objectives': [
                f"Understand core principles of {topic}",
                "Analyze practical applications and time complexities",
                "Complete interactive live coding exercises"
            ],
            'timeline': [
                {'time': '00-10 min', 'section': 'Introduction & Real-world Motivation'},
                {'time': '10-30 min', 'section': 'Theoretical Foundations & Proofs'},
                {'time': '30-45 min', 'section': 'Practical Demonstration & Code Walkthrough'},
                {'time': '45-55 min', 'section': 'Interactive Q&A and Student Problem Solving'},
                {'time': '55-60 min', 'section': 'Assignment Briefing & Next Class Preview'}
            ],
            'recommended_assignments': [
                f"Implement basic module for {topic} (Submit PDF/Code <= 300KB)",
                "Review KNU previous year questions for internal assessment"
            ]
        }
        return jsonify({'success': True, 'lesson_plan': plan})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 400

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8000))
    print(f"Starting BBCSPMS Python AI Service on port {port}...")
    app.run(host='0.0.0.0', port=port, debug=False)
