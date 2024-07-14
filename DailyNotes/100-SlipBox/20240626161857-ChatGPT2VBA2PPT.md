---
aliases: 
theme: 
original: 
url: 
author: 
tags: 
created_date: 
type: 
high priority: false
---
## 通过chatgtp制作PPT
![3 Ways to Create PowerPoi...](https://www.youtube.com/watch?v=JmVWz2PFVA0)
![image.png](https://cdn.jsdelivr.net/gh/duanbiao2000/BlogGallery@main/picture/20240626180602.png)

```prompt
You are an expert in [field/topic].Write an outline for a PowerPoint presentation covering the following [topics].Make it [number]slides

Expand on each of the subtopics you provided earlier.You can consider elaborating on the key ideas,offering supporting examples and explaining any details that you think would enhance the audience's understanding on the topic.

expand the ideas in bullet format and with summary detail

Suggest any images to be included in the slides to enhance the visual appeal.Provide also the Bing Image Creator prompts for the images you suggested
```

### 通过VBA自动生成
```
Write me VBA PowerPoint codes on [topic].Make it [number]slides.
```

```
write VBA codes about the presentation above
```

```VBA
Sub CreateMathCriticalThinkingPresentation()
    Dim pptApp As Object
    Dim pptPres As Object
    Dim slideIndex As Integer
    Dim slide As Object
    
    ' Create a new PowerPoint application
    Set pptApp = CreateObject("PowerPoint.Application")
    pptApp.Visible = True
    
    ' Add a new presentation
    Set pptPres = pptApp.Presentations.Add
    
    ' Slide 1: Title Slide
    slideIndex = slideIndex + 1
    Set slide = pptPres.Slides.Add(slideIndex, 1) ' 1 = ppLayoutTitle
    slide.Shapes.Title.TextFrame.TextRange.Text = "How Mathematics Improves Critical Thinking Skills"
    slide.Shapes.Placeholders(2).TextFrame.TextRange.Text = "Enhancing Analytical Abilities Through Mathematical Practice" & vbCrLf & "Presented by: [Your Name]" & vbCrLf & "Date: [Today's Date]"
    
    ' Slide 2: Introduction
    slideIndex = slideIndex + 1
    Set slide = pptPres.Slides.Add(slideIndex, 2) ' 2 = ppLayoutText
    slide.Shapes.Title.TextFrame.TextRange.Text = "Introduction"
    slide.Shapes.Placeholders(2).TextFrame.TextRange.Text = _
        "Critical Thinking: The ability to analyze, evaluate, and synthesize information to make reasoned decisions." & vbCrLf & _
        "Importance: Essential for problem-solving, decision-making, and effective communication in personal and professional contexts." & vbCrLf & _
        "Mathematics Role: Provides a structured and logical framework to develop and hone these skills."
    
    ' Slide 3: Logical Reasoning
    slideIndex = slideIndex + 1
    Set slide = pptPres.Slides.Add(slideIndex, 2) ' 2 = ppLayoutText
    slide.Shapes.Title.TextFrame.TextRange.Text = "Enhancing Logical Reasoning"
    slide.Shapes.Placeholders(2).TextFrame.TextRange.Text = _
        "Structured Thinking: Mathematics requires step-by-step problem-solving, promoting logical and sequential thinking." & vbCrLf & _
        "Proofs and Theorems: Understanding and constructing proofs develops the ability to reason logically and critically." & vbCrLf & _
        "Example: Solving algebraic equations involves identifying relationships and applying rules systematically."
    
    ' Slide 4: Analytical Skills
    slideIndex = slideIndex + 1
    Set slide = pptPres.Slides.Add(slideIndex, 2) ' 2 = ppLayoutText
    slide.Shapes.Title.TextFrame.TextRange.Text = "Developing Analytical Skills"
    slide.Shapes.Placeholders(2).TextFrame.TextRange.Text = _
        "Data Interpretation: Mathematics involves interpreting data, identifying patterns, and making predictions." & vbCrLf & _
        "Complex Problems: Tackling complex mathematical problems enhances the ability to analyze and break down information into manageable parts." & vbCrLf & _
        "Example: Calculus and statistical analysis require interpreting data trends and understanding underlying principles."
    
    ' Slide 5: Problem-Solving Abilities
    slideIndex = slideIndex + 1
    Set slide = pptPres.Slides.Add(slideIndex, 2) ' 2 = ppLayoutText
    slide.Shapes.Title.TextFrame.TextRange.Text = "Strengthening Problem-Solving Abilities"
    slide.Shapes.Placeholders(2).TextFrame.TextRange.Text = _
        "Abstract Thinking: Mathematics encourages abstract thinking, allowing for the consideration of multiple solutions and approaches." & vbCrLf & _
        "Persistence: Problem-solving in mathematics teaches perseverance and resilience, as it often involves trial and error." & vbCrLf & _
        "Example: Geometry problems often require visualizing shapes and spaces, fostering innovative solutions."
    
    ' Slide 6: Conclusion
    slideIndex = slideIndex + 1
    Set slide = pptPres.Slides.Add(slideIndex, 2) ' 2 = ppLayoutText
    slide.Shapes.Title.TextFrame.TextRange.Text = "Conclusion"
    slide.Shapes.Placeholders(2).TextFrame.TextRange.Text = _
        "Summary: Mathematics significantly enhances critical thinking skills by promoting logical reasoning, analytical abilities, and effective problem-solving." & vbCrLf & _
        "Broader Implications: These skills are transferable to various fields, including science, engineering, economics, and everyday decision-making." & vbCrLf & _
        "Final Thought: Embracing mathematical practice can lead to more structured, logical, and innovative thinking in all aspects of life."
    
    ' Cleanup
    Set slide = Nothing
    Set pptPres = Nothing
    Set pptApp = Nothing
End Sub



```
