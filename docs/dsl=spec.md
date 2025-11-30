(_ QUIZ DSL - GRAMMAR _)

program := quiz_block;

quiz_block := "quiz" "{" quiz_body "}" ;

quiz_body := [ title_stmt ] [ description_stmt ] { question_block } ;

title_stmt := "title" ":" STRING ";" ;

description_stmt := "description" ":" STRING ";" ;

question_block := "question" "{" question_body "}" ;

question_body := text_stmt { choice_stmt } answer_stmt [ difficulty_stmt ] { tag_stmt } ;

text_stmt := "text" ":" STRING ";" ;

choice_stmt := "choice" ":" STRING ";" ;

answer_stmt := "answer" ":" INT ";" ;

difficulty_stmt := "difficulty" ":" STRING ";" ;

tag_stmt := "tag" ":" STRING ";" ;
