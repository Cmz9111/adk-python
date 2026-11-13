# Copyright 2026 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from __future__ import annotations

import logging
from typing import Any

from google.genai import types
from pydantic import alias_generators
from pydantic import BaseModel
from pydantic import ConfigDict

from .cache_metadata import CacheMetadata
from pydantic import Field


### BEGIN_GENERATED_CODE: LlmResponse
### Do not edit, code generation overwrites it.
class LlmResponse(BaseModel):
  """LLM response class that provides the first candidate response from the

  model if available. Otherwise, returns error code and message.

  Attributes:
    content: The content of the response.
    grounding_metadata: The grounding metadata of the response.
    partial: Marks this response as an incomplete fragment of a larger response.
      Only used for streaming mode.
    turn_complete: Indicates whether the response from the model is complete.
      Only used for streaming mode.
    error_code: Error code if the response is an error. Code varies by model.
    error_message: Error message if the response is an error.
    interrupted: Flag indicating that LLM was interrupted when generating the
      content. Usually it's due to user interruption during bidi streaming.
    custom_metadata: The custom metadata of the LlmResponse.
    input_transcription: Audio transcription of user input.
    output_transcription: Audio transcription of model output.
    avg_logprobs: Average log probability of the generated tokens.
    logprobs_result: Detailed log probabilities for chosen and top candidate
      tokens.
  """

  model_config = ConfigDict(
      alias_generator=alias_generators.to_camel,
      extra='forbid',
      populate_by_name=True,
  )
  """The pydantic model config."""

  model_version: str | None = Field(
      default=None,
      description="""Output only. The model version used to generate the response.""",
  )

  content: types.Content | None = Field(
      default=None,
      description="""The generative content of the response.

This should only contain content from the user or the model, and not any
framework or system-generated data.""",
  )

  grounding_metadata: types.GroundingMetadata | None = Field(
      default=None, description="""The grounding metadata of the response."""
  )

  partial: bool | None = Field(
      default=None,
      description="""Marks this response as an incomplete fragment of a larger response.

Only used in streaming mode, where a producer emits zero or more
fragments and then one response with `partial` false or unset that
carries the complete content.

A fragment is a display hint. Its content may be truncated, may be
repeated by the completed response, and may hold a function call whose
arguments have not finished arriving. Nothing may execute a tool, persist
an event, or end a turn based on a fragment.""",
  )

  turn_complete: bool | None = Field(
      default=None,
      description="""Indicates whether the response from the model is complete.
Only used for streaming mode.""",
  )

  turn_complete_reason: types.TurnCompleteReason | None = Field(
      default=None,
      description="""The reason why the turn is complete. Only used for streaming mode.""",
  )

  interaction_status: types.InteractionStatus | None = Field(
      default=None,
      description="""The activity status of the live session, reported with `turn_complete`.

Newer live models may answer a single user prompt with several model
turns, so `turn_complete` alone no longer means the model is done. This
field disambiguates the two:

* `IN_PROGRESS`: the model is still working on the user's prompt; more turns will follow,
  so the app should not treat the interaction as finished (e.g. should not re-enable the
  microphone yet).
* `IDLE`: the model has finished processing the user's prompt and is waiting for further
  user input.

It stays `None` for models that don't report it. Callers building a
turn-taking UI should fall back to treating `turn_complete == True` as
terminal whenever `interaction_status` is `None`.

NOTE: this is not related to the Interactions API
`InteractionStatusUpdate`.""",
  )

  finish_reason: types.FinishReason | None = Field(
      default=None, description="""The finish reason of the response."""
  )

  error_code: str | None = Field(
      default=None,
      description="""Error code if the response is an error. Code varies by model.""",
  )

  error_message: str | None = Field(
      default=None, description="""Error message if the response is an error."""
  )

  interrupted: bool | None = Field(
      default=None,
      description="""Flag indicating that LLM was interrupted when generating the content.
Usually it's due to user interruption during bidi streaming.""",
  )

  custom_metadata: dict[str, Any] | None = Field(
      default=None,
      description="""The custom metadata of the LlmResponse.
An optional key-value map to label an LlmResponse.

NOTE: the entire dict must be JSON-serializable.""",
  )

  usage_metadata: types.GenerateContentResponseUsageMetadata | None = Field(
      default=None, description="""The usage metadata of the LlmResponse."""
  )

  cache_creation_token_count: int | None = Field(
      default=None,
      description="""Number of prompt tokens written to the prompt cache for this response.

The cache-*write* counterpart to
``usage_metadata.cached_content_token_count`` (cache-*read*); both are a
breakdown of ``usage_metadata.prompt_token_count``.

The model backends also attach this value to ``usage_metadata`` as
``cache_creation_input_tokens`` for OpenTelemetry, but ``google.genai``'s
usage type forbids extra fields, so that attribute is dropped on
serialization. This field surfaces the same count on the (serializable)
``LlmResponse`` / ``Event`` so it is visible to the dev UI, persisted
sessions, and other event consumers -- not only telemetry. Only populated
for providers/turns that report cache writes; ``None`` otherwise.""",
  )

  live_session_resumption_update: (
      types.LiveServerSessionResumptionUpdate | None
  ) = Field(
      default=None,
      description="""The session resumption update of the LlmResponse.""",
  )

  live_session_id: str | None = Field(
      default=None, description="""The session ID of the Live session."""
  )

  go_away: types.LiveServerGoAway | None = Field(
      default=None, description="""The GoAway signal from the Live model."""
  )

  voice_activity: types.VoiceActivity | None = Field(
      default=None, description="""Voice activity signal from the Live model."""
  )

  input_transcription: types.Transcription | None = Field(
      default=None, description="""Audio transcription of user input."""
  )

  output_transcription: types.Transcription | None = Field(
      default=None, description="""Audio transcription of model output."""
  )

  avg_logprobs: float | None = Field(
      default=None,
      description="""Average log probability of the generated tokens.""",
  )

  logprobs_result: types.LogprobsResult | None = Field(
      default=None,
      description="""Detailed log probabilities for chosen and top candidate tokens.""",
  )

  cache_metadata: CacheMetadata | None = Field(
      default=None,
      description="""Context cache metadata if caching was used for this response.

Contains cache identification, usage tracking, and lifecycle
information. Automatically populated when context caching is enabled.""",
  )

  citation_metadata: types.CitationMetadata | None = Field(
      default=None,
      description="""Citation metadata for the response.
Automatically populated when citation is enabled.""",
  )

  interaction_id: str | None = Field(
      default=None,
      description="""The interaction ID from the Interactions API.

Populated when using the Interactions API for model invocation to
identify and chain interactions for stateful conversations.""",
  )

  environment_id: str | None = Field(
      default=None,
      description="""The execution environment ID from the Interactions API.

Populated when an Interactions-API agent (e.g. `ManagedAgent`) provisions
or reuses a sandbox environment. It is persisted on the resulting `Event`
so subsequent turns can reuse the same environment for stateful work.""",
  )
  ### END_GENERATED_CODE: LlmResponse

  def get_function_calls(self) -> list[types.FunctionCall]:
    """Returns the function calls in the response."""
    func_calls = []
    if self.content and self.content.parts:
      for part in self.content.parts:
        if part.function_call:
          func_calls.append(part.function_call)
    return func_calls

  def get_function_responses(self) -> list[types.FunctionResponse]:
    """Returns the function responses in the response."""
    func_responses = []
    if self.content and self.content.parts:
      for part in self.content.parts:
        if part.function_response:
          func_responses.append(part.function_response)
    return func_responses

  @staticmethod
  def create(
      generate_content_response: types.GenerateContentResponse,
  ) -> LlmResponse:
    """Creates an LlmResponse from a GenerateContentResponse.

    Args:
      generate_content_response: The GenerateContentResponse to create the
        LlmResponse from.

    Returns:
      The LlmResponse.
    """
    usage_metadata = generate_content_response.usage_metadata
    if generate_content_response.candidates:
      candidate = generate_content_response.candidates[0]
      if (
          candidate.content and candidate.content.parts
      ) or candidate.finish_reason == types.FinishReason.STOP:
        return LlmResponse(
            content=candidate.content,
            grounding_metadata=candidate.grounding_metadata,
            usage_metadata=usage_metadata,
            finish_reason=candidate.finish_reason,
            citation_metadata=candidate.citation_metadata,
            avg_logprobs=candidate.avg_logprobs,
            logprobs_result=candidate.logprobs_result,
            model_version=generate_content_response.model_version,
        )
      else:
        return LlmResponse(
            error_code=candidate.finish_reason,
            error_message=candidate.finish_message,
            citation_metadata=candidate.citation_metadata,
            usage_metadata=usage_metadata,
            finish_reason=candidate.finish_reason,
            avg_logprobs=candidate.avg_logprobs,
            logprobs_result=candidate.logprobs_result,
            model_version=generate_content_response.model_version,
        )
    else:
      if generate_content_response.prompt_feedback:
        prompt_feedback = generate_content_response.prompt_feedback
        return LlmResponse(
            error_code=prompt_feedback.block_reason,
            error_message=prompt_feedback.block_reason_message,
            usage_metadata=usage_metadata,
            model_version=generate_content_response.model_version,
        )
      else:
        # Some model backends can legitimately complete a turn without
        # candidates (for example, tool-driven UI turns with no text). Treat
        # this as an empty successful response rather than an unknown error.
        logging.warning(
            'Received empty candidates and no prompt feedback in model '
            'response. Treating as a successful empty response.'
        )
        return LlmResponse(
            content=types.Content(role='model', parts=[]),
            usage_metadata=usage_metadata,
            model_version=generate_content_response.model_version,
        )
