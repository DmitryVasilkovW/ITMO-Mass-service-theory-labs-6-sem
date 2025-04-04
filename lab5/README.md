### **Практическая работа \#5. Моделирование сети массового обслуживания.**

**Цель работы:**  
Исследовать характеристики сети массового обслуживания, в которой агенты (каналы обслуживания) могут подключаться и отключаться в произвольные моменты времени, с использованием методов имитационного моделирования.

---

### **Задачи:**

1. Разработать многоагентную модель сети массового обслуживания.  
2. Реализовать механизм подключения и отключения агентов (каналов обслуживания).  
3. Провести эксперименты и проанализировать влияние динамики агентов на характеристики сети.

---

### **Исходные данные:**

* Интенсивность входящего потока заявок (λ): задается вариантом (например, 10 заявок/час).  
* Интенсивность обслуживания одного агента (μ): задается вариантом (например, 3 заявки/час).  
* Количество агентов (каналов обслуживания): динамически изменяется от 1 до 5\.  
* Время моделирования: 1000 единиц времени (часы, минуты и т.д., в зависимости от контекста).

---

### **Шаги выполнения работы:**

1. Разработка модели:  
   * Создайте сеть массового обслуживания, состоящую из нескольких узлов.  
   * Реализуйте агентов (каналы обслуживания), которые могут подключаться и отключаться в произвольные моменты времени.  
   * Учтите, что заявки перемещаются между узлами сети в соответствии с заданными вероятностями переходов.  
2. Реализация динамики агентов:  
   * Агенты могут подключаться к сети с заданной интенсивностью (например, 1 агент/час).  
   * Агенты могут отключаться от сети с заданной интенсивностью (например, 0.5 агентов/час).  
   * Учтите, что отключенные агенты не могут обслуживать заявки.  
3. Проведение экспериментов:  
   * Запустите модель для заданных параметров.  
   * Зафиксируйте следующие показатели:  
     * Среднее время пребывания заявки в сети.  
     * Среднее число заявок в очереди.  
     * Среднее число активных агентов.  
     * Вероятность потери заявок (если очередь ограничена).  
4. Анализ результатов:  
   * Проведите анализ влияния динамики агентов на характеристики сети.  
   * Постройте графики зависимости среднего времени пребывания и длины очереди от числа активных агентов.  
   * Сделайте выводы о работе сети и предложите рекомендации по ее оптимизации.

---

### **Требования к отчету:**

1. Описание модели:  
   * Краткое описание сети и ее параметров.  
   * Описание алгоритма работы агентов.  
2. Результаты экспериментов:  
   * Таблицы с данными по каждому эксперименту.  
   * Графики зависимостей характеристик сети от числа активных агентов.  
3. Анализ результатов:  
   * Выводы о работе сети и рекомендации по ее оптимизации.

---

### **Инструменты для выполнения работы:**

* Язык программирования: Python (библиотеки `simpy`, `numpy`, `matplotlib`).  
* Программное обеспечение: AnyLogic, MATLAB (по выбору).

