import tensorflow as tf

# Define the model
model = tf.keras.Sequential([
  tf.keras.layers.Dense(64, activation='relu'),
  tf.keras.layers.Dense(1, activation='sigmoid')
])

# Compile the model
model.compile(optimizer='adam',
              loss='binary_crossentropy',
              metrics=['accuracy'])

# Train the model
model.fit(X, y, epochs=10)

# Make predictions
predictions = model.predict(X)

# Evaluate the model
print(model.evaluate(X, y))
