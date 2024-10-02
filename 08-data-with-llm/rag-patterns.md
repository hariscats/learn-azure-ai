# Fundamental Concepts

### **1. Large Language Models (LLMs)**

- **Definition**: LLMs are AI models designed to understand and generate human language. They are trained on vast amounts of text data and can perform tasks such as text completion, summarization, question answering, and more.
- **Examples**: GPT-3, GPT-4, and BERT are well-known LLMs.
- **Limitation**: LLMs rely on pre-existing knowledge from their training data and can struggle with providing up-to-date or domain-specific information without external data augmentation.

### **2. Data Augmentation for LLMs**

- **Purpose**: Enhancing LLMs with external data to improve their accuracy, reduce hallucinations (fabricated or inaccurate information), and make them more applicable to specialized domains (e.g., legal, medical).
- **Techniques**:
    - **Retrieval-Augmented Generation (RAG)**: Dynamically retrieves relevant information from external databases during the generation process.
    - **Fine-Tuning**: Adjusts the LLM's parameters using domain-specific data to improve performance on specialized tasks.

### **3. Retrieval-Augmented Generation (RAG)**

- **Definition**: A method that combines LLMs with information retrieval systems. It retrieves relevant data from an external source to provide context, which the LLM then uses to generate more accurate and context-aware responses.
- **How It Works**:
    - The LLM first generates a query.
    - Relevant documents or data are retrieved from an external database.
    - The retrieved information is integrated into the LLM’s response generation process.
- **Advantages**: Improves accuracy, reduces hallucinations, and helps handle domain-specific tasks.

### **4. Fine-Tuning**

- **Definition**: The process of training an already pre-trained LLM on additional domain-specific data to adapt it to specialized tasks.
- **Methods**:
    - **Supervised Fine-Tuning**: Uses labeled data (input-output pairs) to train the LLM.
    - **Instruction Tuning**: Fine-tuning the model with instructions to enhance its performance in following commands or prompts.
- **Pros & Cons**:
    - **Pros**: Allows the LLM to learn new information and skills specific to a domain.
    - **Cons**: Resource-intensive and may cause the LLM to forget previously learned knowledge (known as "catastrophic forgetting").

### **5. Query Levels in Data-Augmented LLMs**

Understanding the different types of user queries is crucial for selecting the appropriate data-augmentation technique. Queries are categorized into four levels, each requiring different reasoning capabilities:

1. **Explicit Fact Queries**:
    
    - **Definition**: Queries that can be answered by directly retrieving information from external data.
    - **Example**: "Where is the 2024 Summer Olympics being held?"
    - **Technique**: Basic RAG methods are typically effective.
2. **Implicit Fact Queries**:
    
    - **Definition**: Queries requiring the combination of multiple facts or the application of basic reasoning.
    - **Example**: "What is the capital value of the company Elon Musk founded in 1999?"
    - **Technique**: Iterative RAG or multi-hop retrieval methods are needed.
3. **Interpretable Rationale Queries**:
    
    - **Definition**: Queries that require clear, structured reasoning based on domain-specific guidelines.
    - **Example**: "How should a patient with certain symptoms be treated according to medical guidelines?"
    - **Technique**: Prompt tuning and Chain-of-Thought (CoT) prompting are effective.
4. **Hidden Rationale Queries**:
    
    - **Definition**: The most complex queries requiring the LLM to infer hidden knowledge or strategies from external data.
    - **Example**: "How will the economic situation affect a company's future?"
    - **Technique**: Offline learning, in-context learning, and fine-tuning are necessary.

### **6. Prompt Tuning and Chain-of-Thought (CoT) Prompting**

- **Prompt Tuning**: The process of optimizing prompts to guide the LLM’s responses based on external rationales or guidelines.
- **Chain-of-Thought Prompting**:
    - **Definition**: A technique that encourages the LLM to break down complex tasks into smaller, manageable reasoning steps to arrive at an answer.
    - **Purpose**: Improves the LLM’s ability to handle complex reasoning tasks by following a logical thought process.

### **7. In-Context Learning (ICL)**

- **Definition**: A method where LLMs use examples provided within the prompt (context) to learn how to perform a specific task.
- **How It Works**: By showing the model a few examples of how to solve a problem, the LLM learns the task pattern and applies it to generate an appropriate response.
- **Application**: Helps LLMs adapt to tasks with limited training data or to handle hidden rationale queries more effectively.

### **8. Offline Learning**

- **Definition**: A technique where the LLM learns patterns, rules, or principles from datasets outside the real-time query process.
- **Purpose**: Provides the LLM with accumulated experiences and structured knowledge that can be retrieved to guide reasoning for complex tasks.

### **9. Query-Document Alignment**

- **Definition**: Techniques to align or match user queries with relevant document data to improve information retrieval.
- **Types**:
    - **Traditional Alignment**: Encodes queries and documents separately in a shared vector space.
    - **Doc Domain Alignment**: Generates synthetic documents based on the query’s domain to improve retrieval accuracy.
    - **Query Domain Alignment**: Generates multiple synthetic queries to match how users might frame their questions.

### **10. Multi-Hop Reasoning**

- **Definition**: The process of connecting multiple pieces of information or data points across different sources to answer a query.
- **Use Case**: Common in implicit fact queries where the answer is not directly available but must be inferred from multiple data segments.

### **11. Model Fine-Tuning Integration Strategies**

- **Context-Based Integration**: Injects external data into the LLM’s context window during query processing.
- **Small Model Integration**: Uses a smaller, specialized model to guide the main LLM.
- **Fine-Tuning Integration**: Directly fine-tunes the LLM to become a domain expert model using external knowledge.

### **12. Evaluation Metrics**

- **Evaluation in RAG Systems**: Assessing the accuracy and effectiveness of retrieval-augmented systems can be challenging due to the complexity of tasks and the integration of external data.
- **Performance Indicators**: Metrics like precision, recall, and accuracy are often used, along with more advanced indicators like relevance and coherence.

---

# **Overview**

### **Motivation for External Data in LLMs:**

- **Enhancing Performance**: LLMs perform better in real-world tasks when supplemented with external data, improving their ability to handle domain-specific information and stay current with recent developments.
- **Reducing Hallucinations**: Using external data reduces hallucinations (fabricated or inaccurate information), increasing the accuracy, control, and interpretability of LLM-generated outputs.

### **Techniques for Integrating External Data:**

- **Popular Methods**: Retrieval-Augmented Generation (RAG) and fine-tuning are highlighted as popular strategies for combining LLMs with external data sources.
- **Application Challenges**: Despite their potential, applying these methods effectively in specialized domains is challenging.

### **Challenges in Data-Augmented LLMs:**

- **Retrieving Relevant Data**: Difficulty in retrieving relevant data, understanding user intent, and leveraging LLMs' reasoning abilities for complex tasks.
- **No One-Size-Fits-All**: There's no one-size-fits-all approach; underperformance often results from a mismatch between task requirements and the methods used for data integration.

### **Proposed Task Categorization:**

- **Categorization Levels**:
    - **Explicit Fact Queries**: Direct questions needing clear, factual answers.
    - **Implicit Fact Queries**: Questions requiring understanding of facts not stated explicitly.
    - **Interpretable Rationale Queries**: Tasks needing a clear, interpretable reasoning process.
    - **Hidden Rationale Queries**: Complex queries where the rationale isn't immediately apparent.

### **Forms of Integrating External Data:**

- **Methods**:
    - **Context**: Providing relevant external data as input to the model.
    - **Small Model**: Using smaller, specialized models to complement the LLM.
    - **Fine-Tuning**: Adapting the LLM itself using external data.
- **Strengths and Weaknesses**: Each method has its strengths, limitations, and appropriate use cases.

## **Introduction**

### **Practical Difficulties in Developing Data-Augmented LLMs:**

- Developers face substantial difficulties, such as constructing data pipelines (processing and indexing) and leveraging LLMs for complex reasoning tasks.

### **Domain-Specific Challenges:**

- **Finance**: Requires understanding high-dimensional time-series data.
- **Healthcare**: Involves processing medical images or time-series medical records.
- **Legal and Mathematical Fields**: LLMs struggle with long-distance dependencies and complex logical structures.

### **Need for Customization**:

- A one-size-fits-all approach is ineffective, and developers often overlook domain-specific nuances, leading to flawed solutions.

### **Survey Motivation and Purpose**:

- Existing research focuses on isolated aspects, lacking a holistic view. This survey fills the gap, offering a comprehensive understanding of data-augmented LLM applications.

## **Problem Definition**

### **Four Levels of Queries in Data-Augmented LLMs**

#### **Level 1: Explicit Fact Queries**

- **Description**: Require direct fact retrieval.
- **Example**: "In which country is UEFA EURO 2024 being held?"
- **Challenge**: Finding the exact piece of information.

#### **Level 2: Implicit Fact Queries**

- **Description**: Require combining multiple facts and applying reasoning.
- **Example**: "What is the capital value of the company Elon Musk founded in 1999?"
- **Challenge**: Connecting related facts and applying basic logical reasoning.

#### **Level 3: Interpretable Rationale Queries**

- **Description**: Require understanding and applying domain-specific rationales.
- **Example**: "Do I qualify to apply for a five-year Japanese tourist visa in Shanghai?"
- **Challenge**: Comprehending and applying external rules or guidelines.

#### **Level 4: Hidden Rationale Queries**

- **Description**: Require inferring hidden rationales from patterns in external data.
- **Example**: "How will the economic situation affect the company’s future development?"
- **Challenge**: Discovering hidden rationales and logical chains.

## **Explicit Fact Queries (L1)**

### **Three Types of Query-Document Alignment**

1. **Traditional Alignment**: Encodes queries and documents separately into a shared embedding space.
2. **Doc Domain Alignment**: Generates synthetic documents to match the original query’s domain.
3. **Query Domain Alignment**: Generates synthetic queries that mirror possible ways a question might be framed about document contents.

## **Implicit Fact Queries (L2)**

### **Overview**

- **Definition**: Require synthesizing information from multiple segments or documents.
- **Characteristics**: Involves common-sense reasoning, data aggregation, or multi-hop reasoning.

### **Challenges and Solutions**

- **Adaptive Retrieval Volumes**: Need varying amounts of data.
- **Coordination Between Reasoning and Retrieval**: Must integrate retrieval and reasoning processes intelligently.

#### **Techniques:**

1. **Iterative RAG**: Dynamically retrieves information until the correct answer is found.
2. **Graph/Tree Question Answering**: Represents relationships between data segments as graphs or trees.
3. **Natural Language to SQL**: Converts queries into SQL to retrieve structured data.

## **Interpretable Rationale Queries (L3)**

### **Overview**

- **Definition**: Involves using external data that provides clear, structured rationales.
- **Types of Rationale Data (as shown in Figure 4)**:
    - **Plain Texts**: E.g., Handbooks or guidelines.
    - **Structured Instructions**: E.g., Workflow diagrams, pseudocode.

### **Challenges and Solutions**

- **Prompt Optimization Costs**: Developing tailored prompts is time-consuming.
- **Limited Interpretability**: Understanding the impact of prompts is difficult.

#### **Key Techniques**:

1. **Prompt Tuning**: Enhances LLM’s ability to follow external rationales.
2. **Chain-of-Thought (CoT) Prompting**: Breaks down queries into a sequence of logical steps.
3. **Agent Workflows**: Uses LLMs as part of a larger agent system to manage complex real-world scenarios.

## **Hidden Rationale Queries (L4)**

### **Overview**

- **Definition**: Require understanding implicit, domain-specific reasoning not explicitly stated in data.

### **Key Techniques for Hidden Rationale Queries:**

1. **Offline Learning**: Extracts patterns and principles from datasets offline.
2. **In-Context Learning (ICL)**: Uses example-based learning to enhance LLM performance.
3. **Fine-Tuning**: Adapts LLMs to specific domains using supervised datasets.

### **Injecting Domain-Specific Data into LLMs**

## **Conclusion**

- The paper categorizes data-augmented LLM queries into four distinct levels, each requiring different strategies:
    - **Explicit Fact Queries**: Use RAG.
    - **Implicit Fact Queries**: Use Iterative RAG, RAG on Graph/Tree, and Text-to-SQL.
    - **Interpretable Rationale Queries**: Use Prompt Tuning and CoT Prompting.
    - **Hidden Rationale Queries**: Use Offline Learning, In-Context Learning, and Fine-Tuning.

### **Key Recommendations:**

1. **Understand the Task**: Assess the task’s complexity to select appropriate techniques.
2. **Combine Techniques**: Design routing pipelines integrating multiple methodologies.
3. **Choose the Right Data Injection Strategy**: Use context, small models, or fine-tuning based on the task's requirements.

### **Final Thoughts**

- Building effective data-augmented LLM applications requires understanding the complexity of queries and selecting suitable methodologies. By doing so, developers can create robust solutions tailored to specific real-world challenges.
