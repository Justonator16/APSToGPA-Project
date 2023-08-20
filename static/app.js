function APSLevel(grade){
    if (grade >= 0 && grade <= 29 )
        {
            return 1;
        }
        else if (grade >= 30 && grade <= 39 )
        {
            return 2;
        }
        else if (grade >= 40 && grade <= 49 )
        {
            return 3;
        }
        else if (grade >= 50 && grade <= 59 )
        {
            return 4;
        }
        else if (grade >= 60 && grade <= 69 )
        {
            return 5;
        }
        else if (grade >= 70 && grade <= 79 )
        {
            return 6;
        }
        else (grade >= 80 )
        {
            return 7;
        }
}

function GradeToLetter(grade) {
    /* Common examples of grade conversion are: A+ (97–100), A (93–96), A- (90–92), B+ (87–89), B (83–86), B- (80–82)
    , C+ (77–79)
    , C (73–76)
    , C- (70–72)
    , D+ (67–69)
    , D (65–66),
    D- (below 65). */

    if (grade >= 0 && grade < 60) {
        return "F";
    } else if (grade >= 65 && grade <= 66) {
        return "D";
    } else if (grade >= 67 && grade <= 69) {
        return "D+";
    } else if (grade >= 70 && grade <= 72) {
        return "C-";
    } else if (grade >= 73 && grade <= 76) {
        return "C";
    } else if (grade >= 77 && grade <= 79) {
        return "C+";
    } else if (grade >= 80 && grade <= 82) {
        return "B-";
    } else if (grade >= 83 && grade <= 86) {
        return "B";
    } else if (grade >= 87 && grade <= 89) {
        return "B+";
    } else if (grade >= 90 && grade <= 92) {
        return "A-";
    } else if (grade >= 93 && grade <= 96) {
        return "A";
    } else {
        return "A+";
    }
    }

function GpaScale(grade){

    if (grade >= 0 && grade < 60) {
        return 0.0;
    } else if (grade >= 65 && grade <= 66) {
        return 1.0;
    } else if (grade >= 67 && grade <= 69) {
        return 1.3;
    } else if (grade >= 70 && grade <= 72) {
        return 1.7;
    } else if (grade >= 73 && grade <= 76) {
        return 2.0;
    } else if (grade >= 77 && grade <= 79) {
        return 2.3;
    } else if (grade >= 80 && grade <= 82) {
        return 2.7;
    } else if (grade >= 83 && grade <= 86) {
        return 3.0;
    } else if (grade >= 87 && grade <= 89) {
        return 3.3;
    } else if (grade >= 90 && grade <= 92) {
        return 3.7;
    } else {
        return 4.0;
    }
}

function GetApsScore(){
    let subjects = document.querySelectorAll("#subjects")
    let grades = document.querySelectorAll("#grades")

    /* Get values for each subject and grade using loop  */

    let grade_list = [];
    let aps = 0;
    let distinctions = 0;


    for(let i = 0; i < grades.length; i++)
    {
        if (grades[i].value == '' || subjects[i].value == '')
        {
            alert("Please enter a valid subject and grade.");
            return;
        }
        else
        {
            if ( APSLevel(Number(grades[i].value)) > 6)
            {
                distinctions += 1;
            }
            aps +=  APSLevel(Number(grades[i].value));
            grade_list.push(grades[i].value)
        }
    }

    if (distinctions > 0)
    {
        alert(`Congratulations you got ${distinctions} distinctions. Your APS is ${aps}.`);
        return aps;
    }
    else{
        alert("Your APS is " + aps)
        return aps;
    }
}

function GetApsLevel() {

    let subject = document.querySelector('#subject').value;
    let grade = Number(document.querySelector('#grade').value);

    if (subject == '' || grade == '') {
        alert(`Please enter a valid subject and grade.`);
        return; // Return early if subject or grade is not entered
    }

    if (grade > 100) {
        alert('Invalid grade');
        return; // Return early if grade is invalid
    }

    let apsLevel = APSLevel(grade);

    if (apsLevel == 7){
         // Return the calculated APS level
        alert(`Congratulations you got a distinction in ${subject} and APS level is ${apsLevel}.`);
        return apsLevel;
    }
    else{
        alert(`You got an APS level of ${apsLevel} in ${subject}`);
        return apsLevel;
    }
    }

function GetLetterGrade() {
    let subject = document.querySelector('#subject').value;
    let grade = Number(document.querySelector('#grade').value);

    if (subject === '' || isNaN(grade) || grade < 0 || grade > 100) {
        alert('Please enter a valid subject and grade.');
        return; // Return early if subject or grade is not entered or grade is invalid
    }

    let letter_grade_scale = GradeToLetter(grade);
    alert("You got " + letter_grade_scale + " in " + subject);
    }

function GetGpa(){
    let subjects = document.querySelectorAll('#subjects');
    let grades = document.querySelectorAll('#grades');

    /* GPA = (Sum of grade scale) / (Number of grades) */

    sum_of_gpa_scale = 0

    for(let i = 0; i < grades.length; i++)
    {
        if (grades[i].value == '' || subjects[i].value == '')
        {
            alert('Please enter a valid subject and grade.');
            return;
        }
        else{
            sum_of_gpa_scale += GpaScale(grades[i].value);
        }
    }

    gpa = Math.round((sum_of_gpa_scale / grades.length)* 10)/ 10;

    alert("You have a gpa of "+ gpa);


}

function SaveReportName(){
    let save_report = `
    <div class="content">
        <form action="/aps_score" method="post">
            <input type="text" autocomplete="off" name="transcript" placeholder="Name Latetest Report">
            <button type="submit" onclick="TranscriptName()"><span></span>Save</button>
        </form>
    </div>
`;
    document.querySelector('.response').innerHTML = save_report;

}

function ThankYou(){
    let thank_user = `Thank you for using APSToGPA.`;

    document.querySelector(".response").innerHTML = thank_user;
}

function TranscriptName(){
    let transcript = document.querySelector(".transcript").value;

    if (transcript == ""){
        document.querySelector(".response").innerHTML = `No name found :(`;
    }
}
