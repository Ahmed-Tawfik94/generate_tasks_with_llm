json_schema =""" {
  "properties": {
    "quiz": {
      "type": "object",
      "properties": {
        "task_type": {
          "type": "string"
        },
        "action": {
          "type": "string",
          "description": "similar task type ",
          "value":"quiz"
        },
        "metadata": {
          "type": "object",
          "properties": {
            "questions": {
              "type": "array",
              "items": [
                {
                  "type": "object",
                  "properties": {
                    "success": {
                      "type": "string"
                    },
                    "hint": {
                      "type": "string"
                    },
                    "answers": {
                      "type": "array",
                      "description":" holds 4 choises 1 correct represnted value as 1 and the others are 0 ",
                        "items": [
                        {
                          "type": "object",
                          "properties": {
                            "text": {
                              "type": "string"
                            },
                            "value": {
                              "type": "integer"
                            }
                          },
                          "required": [
                            "text",
                            "value"
                          ]
                        },
                        {
                          "type": "object",
                          "properties": {
                            "text": {
                              "type": "string"
                            },
                            "value": {
                              "type": "integer"
                            }
                          },
                          "required": [
                            "text",
                            "value"
                          ]
                        }
                      ]
                    },
                    "failed": {
                      "type": "string"
                    },
                    "text": {
                      "type": "string"
                    },
                    "answer": {
                      "type": "string"
                    },
                    "type": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "success",
                    "hint",
                    "answers",
                    "failed",
                    "text",
                    "answer",
                    "type"
                  ]
                }
              ]
            },
            "difficulty": {
              "type": "integer"
            },
            "multi_choice": {
              "type": "boolean"
            },
            "hint": {
              "type": "string"
            },
            "caption": {
              "type": "string"
            },
            "intro": {
              "type": "string"
            },
            "tag": {
              "type": "array",
              "items": {}
            },
            "hints": {
              "type": "array",
              "items": [
                {
                  "type": "object",
                  "properties": {
                    "cost": {
                      "type": "number"
                    },
                    "text": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "cost",
                    "text"
                  ]
                }
              ]
            }
          },
          "required": [
            "questions",
            "difficulty",
            "multi_choice",
            "hint",
            "caption",
            "intro",
            "tag",
            "hints"
          ]
        }
      },
      "required": [
        "task_type",
        "action",
        "metadata"
      ]
    },
    "blank": {
      "type": "object",
      "properties": {
        "task_type": {
          "type": "string"
        },
        "action": {
          "type": "string",
          "description": "similar task type ",
          "value":"blank"
        },
        "metadata": {
          "type": "object",
          "properties": {
            "answer": {
              "type": "string",
              "description": "holds the answer of the problem",
            },
            "caption": {
              "type": "string"
            },
            "difficulty": {
              "type": "integer"
            },
            "hint": {
              "type": "string"
            },
            "hints": {
              "type": "array",
              "items": [
                {
                  "type": "object",
                  "properties": {
                    "cost": {
                      "type": "number"
                    },
                    "text": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "cost",
                    "text"
                  ]
                }
              ]
            },
            "intro": {
              "type": "string"
            },
            "precode": {
              "type": "string"
            },
            "problem": {
              "type": "string",
              "description": "the question {{}} as a placeholder for the correct answer",
            },
            "tag": {
              "type": "array",
              "items": {}
            },
            "type": {
              "type": "string"
            }
          },
          "required": [
            "answer",
            "caption",
            "difficulty",
            "hint",
            "hints",
            "intro",
            "precode",
            "problem",
            "tag",
            "type"
          ]
        },
        "code_language": {
          "type": "string"
        }
      },
      "required": [
        "task_type",
        "action",
        "metadata",
        "code_language"
      ]
    },
    "code_python": {
      "type": "object",
      "properties": {
        "metadata": {
          "type": "object",
          "properties": {
            "answer": {
              "type": "array",
              "items": [
                {
                  "type": "object",
                  "properties": {
                    "py": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "py"
                  ]
                }
              ]
            },
            "auto_verify": {
              "type": "boolean"
            },
            "caption": {
              "type": "string"
            },
            "difficulty": {
              "type": "integer"
            },
            "events": {
              "type": "array",
              "items": [
                {
                  "type": "object",
                  "properties": {
                    "caption": {
                      "type": "string"
                    },
                    "key": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "caption",
                    "key"
                  ]
                }
              ]
            },
            "hint": {
              "type": "string"
            },
            "hints": {
              "type": "array",
              "items": [
                {
                  "type": "object",
                  "properties": {
                    "cost": {
                      "type": "number"
                    },
                    "text": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "cost",
                    "text"
                  ]
                }
              ]
            },
            "intro": {
              "type": "string"
            },
            "precode": {
              "type": "object",
              "properties": {
                "py": {
                  "type": "string"
                }
              },
              "required": [
                "py"
              ]
            },
            "problem": {
              "type": "string"
            },
            "tag": {
              "type": "array",
              "items": {}
            },
            "type": {
              "type": "string"
            },
            "verification_type": {
              "type": "string"
            }
          },
          "required": [
            "answer",
            "auto_verify",
            "caption",
            "difficulty",
            "events",
            "hint",
            "hints",
            "intro",
            "precode",
            "problem",
            "tag",
            "type",
            "verification_type"
          ]
        },
        "task_type": {
          "type": "string"
        },
        "code_language": {
          "type": "string"
        }
      },
      "required": [
        "metadata",
        "task_type",
        "code_language"
      ]
    },
    "blank_code": {
      "type": "object",
      "properties": {
        "task_type": {
          "type": "string"
        },
        "action": {
          "type": "string,
          "description": "similar task type ",
          "value":"blank_code"
        },
        "metadata": {
          "type": "object",
          "properties": {
            "answer": {
              "type": "array",
              "items": [
                {
                  "type": "object",
                  "properties": {
                    "py": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "py"
                  ]
                }
              ]
            },
            "caption": {
              "type": "string"
            },
            "update_difficulty": {
              "type": "boolean"
            },
            "difficulty": {
              "type": "integer"
            },
            "events": {
              "type": "array",
              "items": [
                {
                  "type": "object",
                  "properties": {
                    "caption": {
                      "type": "string"
                    },
                    "key": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "caption",
                    "key"
                  ]
                }
              ]
            },
            "language": {
              "type": "string"
            },
            "hint": {
              "type": "string"
            },
            "hints": {
              "type": "array",
              "items": {}
            },
            "intro": {
              "type": "string"
            },
            "precode": {
              "type": "object",
              "properties": {
                "py": {
                  "type": "string"
                }
              },
              "required": [
                "py"
              ]
            },
            "problem": {
              "type": "string"
            },
            "type": {
              "type": "string"
            },
            "tag": {
              "type": "array",
              "items": {}
            },
            "auto_verify": {
              "type": "boolean"
            },
            "solution": {
              "type": "object",
              "properties": {
                "py": {
                  "type": "object",
                  "properties": {
                    "0": {
                      "type": "array",
                      "items": [
                        {
                          "type": "string"
                        }
                      ]
                    }
                  },
                  "required": [
                    "0"
                  ]
                }
              },
              "required": [
                "py"
              ]
            }
          },
          "required": [
            "answer",
            "caption",
            "update_difficulty",
            "difficulty",
            "events",
            "language",
            "hint",
            "hints",
            "intro",
            "precode",
            "problem",
            "type",
            "tag",
            "auto_verify",
            "solution"
          ]
        }
      },
      "required": [
        "task_type",
        "action",
        "metadata"
      ]
    },
    "lecture": {
      "type": "object",
      "properties": {
        "action": {
          "type": "string",
          "description": "similar task type ",
          "value":"lecture"
        },
        "metadata": {
          "type": "object",
          "properties": {
            "auto_verify": {
              "type": "boolean"
            },
            "caption": {
              "type": "string"
            },
            "difficulty": {
              "type": "integer"
            },
            "hint": {
              "type": "string"
            },
            "hints": {
              "type": "array",
              "items": {}
            },
            "intro": {
              "type": "string",
               "description": "hold the introductory to the topic  "
            },
            "problem": {
              "type": "string",
               "description": "holds the lecture knowledge content in markdown "
            },
            "tag": {
              "type": "array",
              "items": {}
            }
          },
          "required": [
            "auto_verify",
            "caption",
            "difficulty",
            "hint",
            "hints",
            "intro",
            "problem",
            "tag"
          ]
        },
        "task_type": {
          "type": "string"
        }
      },
      "required": [
        "action",
        "metadata",
        "task_type"
      ]
    }
  },
  "required": [
    "quiz",
    "blank",
    "code_python",
    "blank_code",
    "lecture"
  ]
}"""

lecture_schema =""""lecture": {
      "type": "object",
      "properties": {
        "action": {
          "type": "string",
          "description": "similar task type ",
          "value":"lecture"
        },
        "metadata": {
          "type": "object",
          "properties": {
            "auto_verify": {
              "type": "boolean"
            },
            "caption": {
              "type": "string"
            },
            "difficulty": {
              "type": "integer"
            },
            "hint": {
              "type": "string"
            },
            "hints": {
              "type": "array",
              "items": {}
            },
            "intro": {
              "type": "string",
               "description": "hold the introductory to the topic  "
            },
            "problem": {
              "type": "string",
               "description": "holds the lecture knowledge content in markdown "
            },
            "tag": {
              "type": "array",
              "items": {}
            }
          }}"""
quiz_schema= """["quizes":{
"type":array,
ïtems:[
"quiz": {
      "type": "object",
      "properties": {
        "task_type": {
          "type": "string"
        },
        "action": {
          "type": "string",
          "description": "similar task type ",
          "value":"quiz"
        },
        "metadata": {
          "type": "object",
          "properties": {
            "questions": {
              "type": "array",
              "items": [
                {
                  "type": "object",
                  "properties": {
                    "success": {
                      "type": "string"
                    },
                    "hint": {
                      "type": "string"
                    },
                    "answers": {
                      "type": "array",
                      "description":" holds 4 choises 1 correct represnted value as 1 and the others are 0 ",
                        "items": [
                        {
                          "type": "object",
                          "properties": {
                            "text": {
                              "type": "string"
                            },
                            "value": {
                              "type": "integer"
                            }
                          },
                          "required": [
                            "text",
                            "value"
                          ]
                        },
                        {
                          "type": "object",
                          "properties": {
                            "text": {
                              "type": "string"
                            },
                            "value": {
                              "type": "integer"
                            }
                          },
                          "required": [
                            "text",
                            "value"
                          ]
                        }
                      ]
                    },
                    "failed": {
                      "type": "string"
                    },
                    "text": {
                      "type": "string"
                    },
                    "answer": {
                      "type": "string"
                    },
                    "type": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "success",
                    "hint",
                    "answers",
                    "failed",
                    "text",
                    "answer",
                    "type"
                  ]
                }
              ]
            },
            "difficulty": {
              "type": "integer"
            },
            "multi_choice": {
              "type": "boolean"
            },
            "hint": {
              "type": "string"
            },
            "caption": {
              "type": "string"
            },
            "intro": {
              "type": "string"
            },
            "tag": {
              "type": "array",
              "items": {}
            }]}"""
python_code_schema ="""[
  "practical":{
"type":array,
ïtems:[ "code_python": {
      "type": "object",
      "properties": {
        "metadata": {
          "type": "object",
          "properties": {
            "answer": {
              "type": "array",
              "items": [
                {
                  "type": "object",
                  "properties": {
                    "py": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "py"
                  ]
                }
              ]
            },
            "auto_verify": {
              "type": "boolean"
            },
            "caption": {
              "type": "string"
            },
            "difficulty": {
              "type": "integer"
            },
            "events": {
              "type": "array",
              "items": [
                {
                  "type": "object",
                  "properties": {
                    "caption": {
                      "type": "string"
                    },
                    "key": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "caption",
                    "key"
                  ]
                }
              ]
            },
            "hint": {
              "type": "string"
            },
            "hints": {
              "type": "array",
              "items": [
                {
                  "type": "object",
                  "properties": {
                    "cost": {
                      "type": "number"
                    },
                    "text": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "cost",
                    "text"
                  ]
                }
              ]
            },
            "intro": {
              "type": "string"
            },
            "precode": {
              "type": "object",
              "properties": {
                "py": {
                  "type": "string"
                }
              },
              "required": [
                "py"
              ]
            },
            "problem": {
              "type": "string"
            },
            "tag": {
              "type": "array",
              "items": {}
            },
            "type": {
              "type": "string"
            },
            "verification_type": {
              "type": "string"
            }
          },
          "required": [
            "answer",
            "auto_verify",
            "caption",
            "difficulty",
            "events",
            "hint",
            "hints",
            "intro",
            "precode",
            "problem",
            "tag",
            "type",
            "verification_type"
          ]
        },
        "task_type": {
          "type": "string"
        },
        "code_language": {
          "type": "string"
        }
      },
      "required": [
        "metadata",
        "task_type",
        "code_language"
      ]
    }]
  }
  
 ]"""