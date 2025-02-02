import json
from datetime import datetime
from typing import Dict, List
import numpy as np
import argparse

class StudentAnalyzer:
    def __init__(self, current_quiz_file: str, historical_quiz_file: str):
        # Load current quiz data
        with open(current_quiz_file, 'r') as file:
            self.current_quiz = json.load(file)
        
        # Load historical quiz data
        with open(historical_quiz_file, 'r') as file:
            historical_data = json.load(file)
        
        # Filter historical data for the current user
        self.user_id = self.current_quiz['user_id']
        self.historical_quizzes = [quiz for quiz in historical_data if quiz['user_id'] == self.user_id]
        
    def analyze_current_performance(self) -> Dict:
        """Analyze the current quiz performance with enhanced metrics"""
        quiz_duration = self._calculate_duration(
            self.current_quiz['started_at'],
            self.current_quiz['ended_at']
        )
        
        current_stats = {
            'accuracy': float(self.current_quiz['accuracy'].strip(' %')),
            'speed': float(self.current_quiz['speed']),
            'raw_score': self.current_quiz['score'],
            'final_score': float(self.current_quiz['final_score']),
            'negative_score': float(self.current_quiz['negative_score']),
            'correct_answers': self.current_quiz['correct_answers'],
            'incorrect_answers': self.current_quiz['incorrect_answers'],
            'total_questions': self.current_quiz['total_questions'],
            'topic': self.current_quiz['quiz']['topic'],
            'mistakes_corrected': self.current_quiz['mistakes_corrected'],
            'initial_mistake_count': self.current_quiz['initial_mistake_count'],
            'trophy_level': self.current_quiz['trophy_level'],
            'better_than_percentile': self.current_quiz['better_than'],
            'duration_minutes': quiz_duration,
            'questions_attempted': len(self.current_quiz['response_map']),
            'rank': self._extract_rank(self.current_quiz['rank_text']),
            'marks_per_question': {
                'correct': float(self.current_quiz['quiz']['correct_answer_marks']),
                'negative': float(self.current_quiz['quiz']['negative_marks'])
            }
        }
        
        return current_stats
    
    def _calculate_duration(self, start_time: str, end_time: str) -> float:
        """Calculate actual duration of quiz attempt in minutes"""
        start = datetime.strptime(start_time, '%Y-%m-%dT%H:%M:%S.%f%z')
        end = datetime.strptime(end_time, '%Y-%m-%dT%H:%M:%S.%f%z')
        return (end - start).total_seconds() / 60
    
    def _extract_rank(self, rank_text: str) -> int:
        """Extract numerical rank from rank text"""
        try:
            return int(rank_text.split('#')[-1])
        except:
            return None

    def analyze_test_taking_strategy(self) -> Dict:
        """Analyze student's test-taking strategy"""
        current_stats = self.analyze_current_performance()
        
        # Calculate time per question
        time_per_question = current_stats['duration_minutes'] / current_stats['questions_attempted']
        
        # Calculate attempt rate
        attempt_rate = (current_stats['questions_attempted'] / 
                       current_stats['total_questions'] * 100)
        
        # Calculate effective score rate
        score_rate = (current_stats['final_score'] / 
                     (current_stats['questions_attempted'] * 
                      current_stats['marks_per_question']['correct']) * 100)
        
        strategy_analysis = {
            'time_management': {
                'time_per_question': round(time_per_question, 2),
                'attempt_rate': round(attempt_rate, 2),
                'is_time_efficient': time_per_question < 1.5  # benchmark of 1.5 minutes per question
            },
            'accuracy_metrics': {
                'score_rate': round(score_rate, 2),
                'negative_marking_impact': round(
                    current_stats['negative_score'] / current_stats['raw_score'] * 100 
                    if current_stats['raw_score'] > 0 else 0, 2
                )
            },
            'attempt_pattern': {
                'questions_attempted': current_stats['questions_attempted'],
                'completion_rate': round(attempt_rate, 2),
                'correct_to_attempt_ratio': round(
                    current_stats['correct_answers'] / 
                    current_stats['questions_attempted'] * 100, 2
                )
            }
        }
        
        return strategy_analysis

    def generate_recommendations(self) -> Dict:
        """Generate enhanced personalized recommendations"""
        current_stats = self.analyze_current_performance()
        strategy_analysis = self.analyze_test_taking_strategy()
        historical_analysis = self.analyze_historical_performance()
        
        recommendations = {
            'priority_actions': [],
            'topic_focus': [],
            'test_strategy': [],
            'improvement_areas': []
        }
        
        # Priority actions based on performance metrics
        if current_stats['negative_score'] > current_stats['raw_score'] * 0.1:
            recommendations['priority_actions'].append(
                "Focus on accuracy over speed - your negative marks are impacting your score significantly"
            )
        
        # Topic focus based on performance
        if current_stats['accuracy'] < 85:
            recommendations['topic_focus'].append(
                f"Dedicate more time to {current_stats['topic']} - aim for at least 85% accuracy"
            )
            
        # Test strategy recommendations
        if strategy_analysis['time_management']['time_per_question'] > 1.5:
            recommendations['test_strategy'].append(
                "Practice time management - aim to spend no more than 1.5 minutes per question"
            )
        
        if strategy_analysis['attempt_pattern']['completion_rate'] < 90:
            recommendations['test_strategy'].append(
                "Work on attempting more questions - you attempted only "
                f"{strategy_analysis['attempt_pattern']['completion_rate']}% of total questions"
            )
            
        # Improvement areas based on mistake patterns
        if current_stats['initial_mistake_count'] > current_stats['mistakes_corrected']:
            recommendations['improvement_areas'].append(
                "Review your mistake patterns - focus on understanding why you made these mistakes"
            )
        
        # Historical performance based recommendations
        if historical_analysis['accuracy_trend'] == 'decreasing':
            recommendations['priority_actions'].append(
                "Your accuracy has been decreasing over time. Focus on consistent practice and review."
            )
        
        if historical_analysis['negative_marking_impact'] > 20:
            recommendations['improvement_areas'].append(
                "Historical data shows a high impact of negative marking. Focus on accuracy."
            )
        
        # Handle first submission case
        if not self.historical_quizzes:
            recommendations['priority_actions'].append(
                "This is your first submission. Focus on building a strong foundation and consistent practice."
            )
        
        return recommendations
    
    def calculate_student_persona(self) -> Dict:
        """Define enhanced student persona based on performance patterns"""
        current_stats = self.analyze_current_performance()
        strategy_analysis = self.analyze_test_taking_strategy()
        historical_analysis = self.analyze_historical_performance()
        
        persona = {
            'performance_level': self._determine_performance_level(current_stats),
            'test_taking_style': self._analyze_test_style(strategy_analysis),
            'competitive_standing': self._evaluate_competitive_position(current_stats),
            'learning_potential': self._assess_learning_potential(current_stats),
            'suggested_focus': self._determine_focus_area(current_stats, strategy_analysis),
            'historical_trends': historical_analysis
        }
        
        return persona
    
    def _determine_performance_level(self, stats: Dict) -> str:
        if stats['accuracy'] >= 90 and stats['better_than_percentile'] > 90:
            return "Top Performer"
        elif stats['accuracy'] >= 75 and stats['better_than_percentile'] > 60:
            return "Strong Performer"
        return "Developing Performer"
    
    def _analyze_test_style(self, strategy: Dict) -> str:
        if strategy['time_management']['is_time_efficient']:
            if strategy['accuracy_metrics']['score_rate'] > 80:
                return "Strategic Speed Solver"
            return "Quick but Needs Accuracy"
        return "Thorough but Needs Speed"
    
    def _evaluate_competitive_position(self, stats: Dict) -> str:
        if stats['better_than_percentile'] > 90:
            return "Top 10% Competitor"
        elif stats['better_than_percentile'] > 75:
            return "Top 25% Competitor"
        return "Developing Competitor"
    
    def _assess_learning_potential(self, stats: Dict) -> str:
        correction_rate = (stats['mistakes_corrected'] / 
                         stats['initial_mistake_count'] 
                         if stats['initial_mistake_count'] > 0 else 1)
        if correction_rate > 0.8:
            return "High Learning Agility"
        elif correction_rate > 0.5:
            return "Moderate Learning Agility"
        return "Needs Learning Support"
    
    def _determine_focus_area(self, stats: Dict, strategy: Dict) -> str:
        if strategy['accuracy_metrics']['negative_marking_impact'] > 20:
            return "Accuracy Improvement"
        elif strategy['attempt_pattern']['completion_rate'] < 80:
            return "Speed Enhancement"
        return "Concept Mastery"

    def analyze_historical_performance(self) -> Dict:
        """Analyze historical quiz performance to identify trends and patterns"""
        if not self.historical_quizzes:
            return {
                'accuracy_trend': 'no data',
                'negative_marking_impact': 0,
                'average_accuracy': 0,
                'average_speed': 0,
                'average_final_score': 0
            }
        
        accuracies = []
        speeds = []
        final_scores = []
        negative_impacts = []
        
        for quiz in self.historical_quizzes:
            accuracy = float(quiz['accuracy'].strip(' %'))
            speed = float(quiz['speed'])
            final_score = float(quiz['final_score'])
            negative_score = float(quiz['negative_score'])
            raw_score = quiz['score']
            
            accuracies.append(accuracy)
            speeds.append(speed)
            final_scores.append(final_score)
            negative_impacts.append(negative_score / raw_score * 100 if raw_score > 0 else 0)
        
        # Determine accuracy trend
        if len(accuracies) > 1:
            accuracy_trend = 'increasing' if accuracies[-1] > accuracies[0] else 'decreasing'
        else:
            accuracy_trend = 'no trend'
        
        return {
            'accuracy_trend': accuracy_trend,
            'negative_marking_impact': round(np.mean(negative_impacts), 2),
            'average_accuracy': round(np.mean(accuracies), 2),
            'average_speed': round(np.mean(speeds), 2),
            'average_final_score': round(np.mean(final_scores), 2)
        }

# Argument parsing
def parse_arguments():
    parser = argparse.ArgumentParser(description="Analyze student quiz performance and provide recommendations.")
    parser.add_argument('--current', type=str, required=True, help="Path to the current quiz JSON file.")
    parser.add_argument('--historical', type=str, required=True, help="Path to the historical quizzes JSON file.")
    return parser.parse_args()

# Example usage
if __name__ == "__main__":
    args = parse_arguments()
    
    # Initialize with provided quiz data files
    analyzer = StudentAnalyzer(args.current, args.historical)
    
    # Get detailed analysis
    performance = analyzer.analyze_current_performance()
    strategy = analyzer.analyze_test_taking_strategy()
    recommendations = analyzer.generate_recommendations()
    persona = analyzer.calculate_student_persona()
    
    print("Performance Analysis:", json.dumps(performance, indent=4))
    print("\nTest Strategy Analysis:", json.dumps(strategy, indent=4))
    print("\nPersonalized Recommendations:", json.dumps(recommendations, indent=4))
    print("\nStudent Persona:", json.dumps(persona, indent=4))