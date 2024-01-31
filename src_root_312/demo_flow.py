{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f0d4795c-d123-4237-b5f8-967cdf718416",
   "metadata": {},
   "outputs": [],
   "source": [
    "import prefect\n",
    "from prefect import task, Flow\n",
    "\n",
    "# 定义任务\n",
    "@task\n",
    "def extract():\n",
    "    return [1, 2, 3, 4, 5]\n",
    "\n",
    "@task\n",
    "def transform(data):\n",
    "    return [x * 10 for x in data]\n",
    "\n",
    "@task\n",
    "def load(data):\n",
    "    print(\"Final Result: {}\".format(data))\n",
    "\n",
    "# 定义数据工作流\n",
    "with Flow(\"demo-flow\") as flow:\n",
    "    data = extract()\n",
    "    transformed_data = transform(data)\n",
    "    load(transformed_data)\n",
    "\n",
    "# 在Jupyter Notebook中运行工作流\n",
    "flow.run()\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.1"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
