### **Практическая работа \#1. Анализ одноканальной системы с отказами.**

**Цель работы:**  
Исследовать характеристики одноканальной системы массового обслуживания с отказами (M/M/1/0) с использованием методов имитационного моделирования.

---

### **Задачи:**

1. Разработать имитационную модель одноканальной системы с отказами.  
2. Провести эксперименты с различными параметрами системы.  
3. Проанализировать полученные результаты и сделать выводы.

---

### **Исходные данные:**

* Интенсивность входящего потока заявок (λ): задается вариантом (например, 5 заявок/час).  
* Интенсивность обслуживания (μ): задается вариантом (например, 6 заявок/час).  
* Время моделирования: 1000 единиц времени (часы, минуты и т.д., в зависимости от контекста).

---

### **Шаги выполнения работы:**

1. **Разработка модели:**  
   * Создайте имитационную модель одноканальной системы с отказами.  
   * Учтите, что если заявка поступает в момент, когда канал занят, она теряется.  
   * Используйте генератор случайных чисел для моделирования входящего потока и времени обслуживания.  
2. **Проведение экспериментов:**  
   * Запустите модель для заданных значений λ и μ.  
   * Зафиксируйте следующие показатели:  
     * Количество поступивших заявок.  
     * Количество обслуженных заявок.  
     * Количество потерянных заявок.  
     * Вероятность отказа (доля потерянных заявок).  
     * Коэффициент загрузки системы (доля времени, когда канал занят).  
3. **Анализ результатов:**  
   * Сравните полученные экспериментальные значения с теоретическими расчетами (используйте формулу Эрланга для вероятности отказа).  
   * Постройте графики зависимости вероятности отказа от интенсивности входящего потока (λ) при фиксированном μ.  
   * Сделайте выводы о влиянии параметров λ и μ на характеристики системы.

---

### **Требования к отчету:**

1. Описание модели:  
   * Краткое описание системы и ее параметров.  
   * Алгоритм работы модели.  
2. Результаты экспериментов:  
   * Таблицы с данными по каждому эксперименту.  
   * Графики зависимости вероятности отказа от λ.  
3. Анализ результатов:  
   * Сравнение экспериментальных и теоретических значений.  
   * Выводы о работе системы.

---

### **Инструменты для выполнения работы:**

* Язык программирования: Python (библиотеки `numpy`, `matplotlib`, `simpy`).  
* Программное обеспечение: AnyLogic, MATLAB, Simulink (по выбору).

